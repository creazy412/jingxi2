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
        'cookie': 'wxa_level=1; webp=1; block_call_jdapp=11; sc_width=1920; __jdv=122270672%7Cbaidu%7C-%7Corganic%7Cnot%20set%7C1587518294267; wq_area=19_1607_4773%7C3; visitkey=28627513144879948; shshshfpa=f332fdcd-560b-5bf8-3c9c-9677b27ae4dc-1587518295; shshshfpb=cGa6CPa3nfOg4kZFPlxG7dg%3D%3D; retina=1; TrackerID=MRD4qz0xN_u4iyYh57criOB8RYViUMbilLbqHS-4SuSuZZt_Kgfbt2xCFiPLQs166V_pjsOIH-T9I59R8GM31wbjswcGtoPWdaXPtZ6T_0cTKfT73tYYU2gwVa3FpIHcHQ0Y44b-riLPOEypZgtgrw; pt_key=AAJen56gADB36nGmzYAiSsxxG7Sr8eynyZLVnz4lvzMMHGrhaaUQ-MW4YaHzpM1jVBoHaTAWmGU; pt_pin=jd_RmVTvMkeKfWf; pt_token=oycwt392; pwdt_id=jd_RmVTvMkeKfWf; cid=9; shshshfp=d54b79c8c57595c77d64b2e240e58999; PPRD_P=CT.138631.36.18; wqmnx1=MDEyNjM4Ni8uaS90ZTIxOC9ucjs1TUFLM0xHaC4xbGkxc2Y0MkVIJlI%3D; __wga=1587519170074.1587518294262.1587518294262.1587518294262.6.1; shshshsID=d95841118172c6fbf1f8021ff08af228_8_1587519170368; promotejs=f2a688c4db2653493d6d3cf04e008e95H*1348LJ%25',
    }

    params = (
        ('active', 'zhiboduihuanhb' + activeDate),
        ('level', '3'), # 1 20元红包、2 10元红包、3 5元红包、4 2元红包、5 1元红包
        ('platform', '4'),
        ('_', microsecond),
        ('sceneval', '2'),
        ('g_login_type', '1'),
        ('callback', 'jsonpCBKR'),
        ('g_ty', 'ls'),
    )

    response = requests.get('https://wq.jd.com/jxlivetask/DrawAward', headers=headers, params=params)
    localtime = time.asctime( time.localtime(time.time()) )

    # 根据返回结果处理
    resultText = response.text.replace('jsonpCBKR(', '')
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
        hourTimestampPlus30 = int(time.mktime(hourTimestampArray) + 30)

        # 开始时间点
        startLoopPoint = time.strftime("%Y-%m-%d 23:59:55", time.localtime())
        startLoopPointArray = time.strptime(startLoopPoint, "%Y-%m-%d %H:%M:%S")
        startLoopPointTimestamp = int(time.mktime(startLoopPointArray))
        # print(startLoopPointTimestamp)
        # 当前时间在 T 23:59:55 --- T+1 00:00:30 之间
        if (currentTimestamp > startLoopPointTimestamp and currentTimestamp <= (startLoopPointTimestamp + 5)) or (currentTimestamp >= hourTimestamp and currentTimestamp < hourTimestampPlus30):
            exchange()
            time.sleep(1)

def main():
    # 调用
    cycle()
    
if __name__ == "__main__":
    main()
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://wq.jd.com/jxlivetask/DrawAward?active=zhiboduihuanhb2020412&level=1&platform=4&_=1586652179175&sceneval=2&g_login_type=1&callback=jsonpCBKM&g_ty=ls', headers=headers, cookies=cookies)
