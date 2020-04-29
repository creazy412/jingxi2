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
        'cookie': 'webp=1; sc_width=1920; visitkey=28627513144879948; shshshfpa=f332fdcd-560b-5bf8-3c9c-9677b27ae4dc-1587518295; shshshfpb=cGa6CPa3nfOg4kZFPlxG7dg%3D%3D; retina=1; __jda=122270672.15881431483991546161782.1588143148.1588143148.1588143148.1; __jdc=122270672; __jdv=122270672|baidu|-|organic|not set|1588143148402; areaId=19; wxa_level=1; TrackerID=01HToTouMIMHFimdWvPmTsZ1lCb3OidpxnSvQO6HXslr8ZVUBWde9X22QpgeJek-hz08SHp9x-_WetwMfHQDfaoFCcwGkBotAQomhc4YppVy2t8gJeaAVv70iQQXaQCS; pt_key=AAJeqXopADCSgr1TwFkDuwFeFmvdpC7IAmpkL0kQeJL1_95Baq2ioVCaJtRfDotT1SquqnhA3CI; pt_pin=754634469_m; pt_token=xjnpfv8x; pwdt_id=754634469_m; cid=9; shshshfp=5e79c84a53b444d501f6360f39661581; block_call_jdapp=11; PPRD_P=CT.138631.36.18-UUID.15881431483991546161782; wqmnx1=MDEyNjM3MGgvLmxzeHNsNjQ4YUxBIGVCUkFiN0hpa28wMWlhLjMyVUIyUkkqKSU%3D; __wga=1588165198962.1588165058208.1588162700208.1587518294262.7.6; shshshsID=c6eec676d48c355868fc2c3563a7ec5a_8_1588165200338; promotejs=354e923c848a8a5478d5d793bab74c69484',
    }

    params = (
        ('active', 'zhiboduihuanhb' + activeDate),
        ('level', '4'), # 1 20元红包、2 10元红包、3 5元红包、4 2元红包、5 1元红包
        ('platform', '4'),
        ('_', microsecond),
        ('sceneval', '2'),
        ('g_login_type', '1'),
        ('callback', 'jsonpCBKM'),
        ('g_ty', 'ls'),
    )

    response = requests.get('https://wq.jd.com/jxlivetask/DrawAward', headers=headers, params=params)
    localtime = time.asctime( time.localtime(time.time()) )

    # 根据返回结果处理
    resultText = response.text.replace('jsonpCBKM(', '')
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
        hourTimestampFormat = time.strftime("%Y-%m-%d 00:00:02", time.localtime())
        hourTimestampArray = time.strptime(hourTimestampFormat, "%Y-%m-%d %H:%M:%S")
        hourTimestamp = int(time.mktime(hourTimestampArray))
        hourTimestampPlus1 = int(time.mktime(hourTimestampArray) + 1)

        # 开始时间点
        startLoopPoint = time.strftime("%Y-%m-%d 23:59:55", time.localtime())
        startLoopPointArray = time.strptime(startLoopPoint, "%Y-%m-%d %H:%M:%S")
        startLoopPointTimestamp = int(time.mktime(startLoopPointArray))
        # print(startLoopPointTimestamp)
        # 当前时间在 T 23:59:55 --- T+1 00:00:30 之间
        if (currentTimestamp >= hourTimestamp and currentTimestamp <= hourTimestampPlus1):
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
