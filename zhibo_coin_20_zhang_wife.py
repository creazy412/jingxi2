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
    cookies = {
        'wxa_level': '1',
        'retina': '0',
        'cid': '9',
        'wqmnx1': 'MDEyNjM4Ni8uaS90ZTE3OS8xdSAgKTIgLzM3YTVXRFUp',
        'webp': '1',
        '__jda': '122270672.1587649229460465590896.1587649229.1587649229.1587649229.1',
        '__jdb': '122270672.8.1587649229460465590896|1.1587649229',
        '__jdv': '122270672%7Cdirect%7C-%7Cnone%7C-%7C1587649229461',
        '__jdc': '122270672',
        'mba_muid': '1587649229460465590896',
        'mba_sid': '15876492294628876587270520362.8',
        '__wga': '1587649523649.1587649229621.1587649229621.1587649229621.6.1',
        'PPRD_P': 'UUID.1587649229460465590896-CT.138631.36.18',
        'sc_width': '1920',
        'shshshfp': '541681cac3438f7d8b66828a686e1a7a',
        'shshshfpa': '913631a5-b454-e8b1-e4a9-1a708e6c7159-1587649230',
        'shshshsID': 'fc7cac4170c307cdd8707889533a9a2d_6_1587649523890',
        'shshshfpb': 'g7ZQ19H68KgGIG2wtlgoseg%3D%3D',
        'TrackerID': 'gQfAzvhxw17wvpb2nG7eWsatLPiTDiJwZQqvrm3snfKeO_7o7l9pBQ3zX4E_FOyC4zr0BGDgIzI4IwAwnl_yEeFRRaoRWMFa7UXG7L-9SYHnv_ZAcPuvwnvyVa3zCAwSP48FqoFxdi85dNLw-Sy1fA',
        'pt_key': 'AAJeoZtrADDg-FrsSxTv3z2GdFQN4z4vwLNqTJWVYXL-zu_e5DKJ2Q7Lr3pxguvsB3iREE2IEDg',
        'pt_pin': 'jd_735dea6726554',
        'pt_token': 'dkze7qks',
        'pwdt_id': 'jd_735dea6726554',
        'visitkey': '17274183726511859',
        'block_call_jdapp': '11',
        'promotejs': '357c4c447bc6d8a294869a1842c22f7eH*1348LJ%25',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Referer': 'https://wqs.jd.com/pglive/task/index.html?sceneval=2',
    }

    params = (
        ('active', 'zhiboduihuanhb' + activeDate),
        ('level', '1'), # 1 20元红包、2 10元红包、3 5元红包、4 2元红包、5 1元红包
        ('platform', '4'),
        ('_', microsecond),
        ('sceneval', '2'),
        ('g_login_type', '1'),
        ('callback', 'jsonpCBKH'),
        ('g_ty', 'ls'),
    )
    
    response = requests.get('https://wq.jd.com/jxlivetask/DrawAward', headers=headers, params=params, cookies=cookies)
    localtime = time.asctime( time.localtime(time.time()) )

    # 根据返回结果处理
    resultText = response.text.replace('jsonpCBKH(', '')
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
        # 当前时间在 T 23:59:55 --- T+1 00:00:30 之间
        if (currentTimestamp >= hourTimestamp and currentTimestamp < hourTimestampPlus1):
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
