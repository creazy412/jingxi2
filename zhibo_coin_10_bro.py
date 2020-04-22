import requests
import time
import datetime
import sys
import json

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
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36',
        'sec-fetch-dest': 'script',
        'accept': '*/*',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'no-cors',
        'referer': 'https://wqs.jd.com/pglive/task/index.html?sceneval=2',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'shshshfpa=490f7e17-1abe-d98b-e7ad-820b5f44f42f-1571622018; shshshfpb=khsT03U5oDfyZ%2FoU01w2Bfw%3D%3D; pinId=p9q4GZ0bvhUviOw3JTn08g; __jdu=1433937085; __jdv=76161171%7Cbaidu%7C-%7Corganic%7Cnot%20set%7C1586093544852; TrackID=1H6V0HWVPQH1CTcFqAalsPMA_2Yl6dGufZZX4pjjLKXbVyhbCwXEJDgDlvxINjb782x7OPHVMXmGjcinyVtp61E3oYjS7DgjtzNdfn8kT4Fo; pin=754634469_m; unick=%E7%8C%AE%E6%B6%9B%E5%8B%87; _tp=%2BWZS%2FWDHCOCSXWgN63a%2BSw%3D%3D; _pst=754634469_m; __jdc=76161171; __jda=76161171.1433937085.1565602967.1586224508.1586246687.26; webp=1; visitkey=43179755944294334; sc_width=400; block_call_jdapp=11; 3AB9D23F7A4B3C9B=UHLJPPNJYGNUTGKGPQXUX57EJ4ZH2RY725YSYIBMXHRXKS2L3PEIWIRWDYNB3FNKX6MZQHMUWVI232ZXYIKIYB3H34; retina=1; wxa_level=1; TrackerID=ELz8f52kxCJVvv5zcb3fxXF5XDZyz1QwCq2J4ncwGev9vgJG84EApiO73CzcIfc4sa3eL1trF6syNVjsN0F5E3YaSi1FHNEK9hgg5RPu3v2Am2zD9jTTU2rVvwBz0YJ7oU7-RNmcR0rRmgsW-dD9IA; pt_key=AAJenEaUADDW-ODAs55rznqTAGHRyRoGMac-bbCyctOjgUtaqTb71JeHxBFcU44LdT08NIYtaLs; pt_pin=jd_RmVTvMkeKfWf; pt_token=mbmervo3; pwdt_id=jd_RmVTvMkeKfWf; cid=9; shshshfp=63dc7904ead941e56020457b351c26bf; PPRD_P=UUID.1433937085-CT.138631.36.18; wqmnx1=MDEyNjM3NTpqcHRkbHY0NTNsIDtpIDUvKVc1KCBlaDA3b2EzNVlmLTRZRCMoSA%3D%3D; __wga=1587304110256.1587304110256.1587299218609.1586247616596.1.11; shshshsID=ab03e0ead59ba6d33b15727b2bb56ce3_1_1587304110657; promotejs=dad25d9cb0df11def095614747027d2aaSd412kSd',
    }

    params = (
        ('active', 'zhiboduihuanhb' + activeDate),
        ('level', '2'), # 1 20元红包、2 10元红包、3 5元红包、4 2元红包、5 1元红包
        ('platform', '4'),
        ('_', microsecond),
        ('sceneval', '2'),
        ('g_login_type', '1'),
        ('callback', 'jsonpCBKL'),
        ('g_ty', 'ls'),
    )

    response = requests.get('https://wq.jd.com/jxlivetask/DrawAward', headers=headers, params=params)
    localtime = time.asctime( time.localtime(time.time()) )

    # 根据返回结果处理
    resultText = response.text.replace('jsonpCBKL(', '')
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
