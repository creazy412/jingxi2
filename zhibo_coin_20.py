import requests
import time
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import sys
from util import *

def exchange():
    t = time.time()
    microsecond = int(round(t * 1000))
    activeDate = time.strftime("%Y%#m%d", time.localtime())

    """
    替换
    """
    cookies = {
        '__jdu': '15510555295861266323195',
        'shshshfpa': '35670fbc-6fb1-0e99-5b6c-1d92b073e604-1551055531',
        'shshshfpb': 'kkDG3ocAfgjv1kYR55cL6GQ%3D%3D',
        '3AB9D23F7A4B3C9B': 'YAZYEV2VJOD6QJZM7WBS3G7ATMRXMBWGI6TCSUILAI3AQVTIJJWK7G4MZU3HILXX3ZRGORRWNL6KDUCX45I3SLIVGM',
        'webp': '1',
        'visitkey': '20405373257032906',
        '__jda': '122270672.15510555295861266323195.1551055530.1578145679.1583414707.5',
        'wxa_level': '1',
        'block_call_jdapp': '11',
        '__jdv': '122270672%7Cbaidu%7C-%7Corganic%7Cnot%20set%7C1586649190834',
        'sc_width': '1536',
        'wq_area': '53283_53440_0%7C0',
        'TrackerID': '0tHcRgNngOnNGDBkK-5FrIAdu6cXCI6eD3GNZ_-AFH8w8Onp-EBRU-dp-31ThJmTmuZsHug8Jc40TuUAsfCo1xfYQItcMbFg_Jz77Tdsh3lJHHEhuL5Rkb3q_e4zDLwD',
        'pt_key': 'AAJekloaADCA6o9CfSSn-lEonQds5nngGCVfgiFZ7RnhqN2BfHuqwvL0qxrze_AYKV_FQ0NRU1Y',
        'pt_pin': '754634469_m',
        'pt_token': '838vz8v3',
        'pwdt_id': '754634469_m',
        'retina': '1',
        'cid': '9',
        'PPRD_P': 'UUID.15510555295861266323195-FOCUS.FO4O305%3ABOCE2543O575AA4O76DB4O2DBE3O23O1%3AFOFO9O17O1FOFO6382CO76DBBOCE2547C01A30CE2CE0627-CT.138631.36.18',
        'shshshfp': '09ee4b5c2bf619958f363e58d2e43363',
        'wqmnx1': 'MDEyNjM2M3BxY2xhZG1uMjA1MGwwdWQ2ZSAvTmxpLkhsZUMvMzNpZjMzZjRmQktZQ0ZGKCU%3D',
        '__wga': '1586652140790.1586649190828.1583414565242.1583414565242.12.2',
        'shshshsID': 'dcab6953f600e143916ad8ca71f3fdb0_13_1586652143907',
        'promotejs': 'c8d693fcf349bee790cc93ec6cb2dfa3aZd1036kBd',
    }

    """
    替换
    """
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36',
        'Sec-Fetch-Dest': 'script',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'no-cors',
        'Referer': 'https://wqs.jd.com/pglive/task/index.html?sceneval=2',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    params = (
        ('active', 'zhiboduihuanhb' + activeDate),
        ('level', '1'), # 1 20 元的优惠券
        ('platform', '4'),
        ('_', microsecond),
        ('sceneval', '2'),
        ('g_login_type', '1'),
        ('callback', 'jsonpCBKM'),
        ('g_ty', 'ls'),
    )

    response = requests.get('https://wq.jd.com/jxlivetask/DrawAward', headers=headers, params=params, cookies=cookies)
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
        hourTimestampFormat = time.strftime("%Y-%m-%d %H:00:00", time.localtime())
        hourTimestampArray = time.strptime(hourTimestampFormat, "%Y-%m-%d %H:%M:%S")
        # print(hourTimestampArray)
        hourTimestamp = int(time.mktime(hourTimestampArray) + 30)
        if currentTimestamp > hourTimestamp:
            # print('currentTimestamp ', currentTimestamp)
            # print(hourTimestamp)
            # print('continue', loopCounter)
            # loopCounter += 1
            continue
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
