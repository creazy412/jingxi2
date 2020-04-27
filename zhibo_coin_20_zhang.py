import requests
import time
import datetime
import sys
import json
from datetime import datetime

def exchange():
    t = time.time()
    microsecond = int(round(t * 1000))
    # activeDate = time.strftime("%Y%#m%d", time.localtime())

    now = datetime.now()
    year = str(int(now.strftime('%Y')))
    month = str(int(now.strftime('%m')))
    day = str(now.strftime('%d'))
    activeDate = year + '' + month + '' + day

    """
    替换
    """
    headers = {
        'authority': 'wq.jd.com',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Mobile Safari/537.36',
        'accept': '*/*',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-dest': 'script',
        'referer': 'https://wqs.jd.com/pglive/task/index.html?sceneval=2',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'webp=1; sc_width=1920; __jdv=122270672%7Cbaidu%7C-%7Corganic%7Cnot%20set%7C1587518294267; visitkey=28627513144879948; shshshfpa=f332fdcd-560b-5bf8-3c9c-9677b27ae4dc-1587518295; shshshfpb=cGa6CPa3nfOg4kZFPlxG7dg%3D%3D; retina=1; cid=9; TrackerID=0rf15RHd1F2JEPV_5CCRbAD1_aIpWqax-UfiTVOuHfPwDLFaCx-ntcsU1rfTzMIzhJQ4ZJfrV79NaZbWiVrfDsg_VSjjs7TrrhsV2UgxeCRrEUOrU4VSqTcq0E6wL_qvAhQIGJ9bjvW7RhAcAzBKjQ; pt_key=AAJeoZxiADA8MMr-YZUjtwQU3PbjdOmDIikJGliev2m3Gwk8ICYiZwUC-g12ASReh32o3Yb9Glk; pt_pin=jd_4fa165b2f7d17; pt_token=v48lnx1l; pwdt_id=jd_4fa165b2f7d17; PPRD_P=CT.138631.36.18; wxa_level=1; wqmnx1=MDEyNjM5OHdtdHhlMjFNLjsgdWQgSzYga2U0YnIxWVU0V1NIKQ%3D%3D; __wga=1587948469604.1587948469604.1587906424381.1587518294262.1.4; shshshfp=5e79c84a53b444d501f6360f39661581; shshshsID=f36e9d751eba63355d170a79c650c89c_1_1587948471920; promotejs=c9ab620d01595f6d7040d95ae8a006d617CIT',
    }

    params = (
        ('active', 'zhiboduihuanhb' + activeDate),
        ('level', '1'), # 1 20元红包、2 10元红包、3 5元红包、4 2元红包、5 1元红包
        ('platform', '4'),
        ('_', microsecond),
        ('sceneval', '2'),
        ('g_login_type', '1'),
        ('callback', 'jsonpCBKN'),
        ('g_ty', 'ls'),
    )
    
    response = requests.get('https://wq.jd.com/jxlivetask/DrawAward', headers=headers, params=params)
    localtime = time.asctime( time.localtime(time.time()) )

    # 根据返回结果处理
    resultText = response.text.replace('jsonpCBKN(', '')
    resultText = resultText.replace(')', '')
    resultText = resultText.replace(';', '')
    resultTextJson = json.loads(resultText)
    if resultTextJson['msg'] == 'success':
        print(localtime, '兑换成功！')
        exit()

    print(localtime, '兑换结果:', response.text)

def cycle():
    """
    循环调用
    如果当前时间大于整点+30秒的时候 continue
    """
    while True:
        currentTimestamp = int(time.time())
        hourTimestampFormat = time.strftime("%Y-%m-%d 00:00:00", time.localtime())
        hourTimestampArray = time.strptime(hourTimestampFormat, "%Y-%m-%d %H:%M:%S")
        hourTimestamp = int(time.mktime(hourTimestampArray))
        hourTimestampPlus1 = int(time.mktime(hourTimestampArray) + 1)

        # 开始时间点
        startLoopPoint = time.strftime("%Y-%m-%d 23:59:59", time.localtime())
        startLoopPointArray = time.strptime(startLoopPoint, "%Y-%m-%d %H:%M:%S")
        startLoopPointTimestamp = int(time.mktime(startLoopPointArray))
        # print(startLoopPointTimestamp)
        # 当前时间在 T 23:59:55 --- T+1 00:00:01 之间
        if (currentTimestamp > startLoopPointTimestamp and currentTimestamp <= (startLoopPointTimestamp + 1)) or (currentTimestamp >= hourTimestamp and currentTimestamp <= hourTimestampPlus1):
            exchange()
            time.sleep(0.5)

def main():
    # 调用
    cycle()
    
if __name__ == "__main__":
    main()
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://wq.jd.com/jxlivetask/DrawAward?active=zhiboduihuanhb2020412&level=1&platform=4&_=1586652179175&sceneval=2&g_login_type=1&callback=jsonpCBKM&g_ty=ls', headers=headers, cookies=cookies)
