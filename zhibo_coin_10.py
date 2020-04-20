import requests
import time
import datetime
import sys
import json

def exchange():
    t = time.time()
    microsecond = int(round(t * 1000))
    activeDate = time.strftime("%Y%#m%d", time.localtime())

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
        'cookie': 'shshshfpa=490f7e17-1abe-d98b-e7ad-820b5f44f42f-1571622018; shshshfpb=khsT03U5oDfyZ%2FoU01w2Bfw%3D%3D; pinId=p9q4GZ0bvhUviOw3JTn08g; __jdu=1433937085; __jdv=76161171%7Cbaidu%7C-%7Corganic%7Cnot%20set%7C1586093544852; TrackID=1H6V0HWVPQH1CTcFqAalsPMA_2Yl6dGufZZX4pjjLKXbVyhbCwXEJDgDlvxINjb782x7OPHVMXmGjcinyVtp61E3oYjS7DgjtzNdfn8kT4Fo; pin=754634469_m; unick=%E7%8C%AE%E6%B6%9B%E5%8B%87; _tp=%2BWZS%2FWDHCOCSXWgN63a%2BSw%3D%3D; _pst=754634469_m; __jdc=76161171; __jda=76161171.1433937085.1565602967.1586224508.1586246687.26; webp=1; visitkey=43179755944294334; sc_width=400; block_call_jdapp=11; 3AB9D23F7A4B3C9B=UHLJPPNJYGNUTGKGPQXUX57EJ4ZH2RY725YSYIBMXHRXKS2L3PEIWIRWDYNB3FNKX6MZQHMUWVI232ZXYIKIYB3H34; retina=1; TrackerID=77OnRyyhaIxQ6YgCV3-Q6x3OD1Mnxzrmxh1J_oWlpaqTB8mGnO_Fea_5b_GEdh-F58yWSt2YVtol24vYKDOtX3Z8bvA3u6tLqi0MX20XDZ2dcM0kLUZwSHex3nnbg9S0auQAD4E8Ojub9nrTRWyKyw; pt_key=AAJelGk-ADATQxnhjDbBnBf7DaZRy0U6kA87pIredOWl35SUOFU42iVXrPECT4BAFu5NC3aywVw; pt_pin=jd_478f44263fce3; pt_token=n4zk9w5j; pwdt_id=jd_478f44263fce3; wxa_level=1; cid=9; shshshfp=63dc7904ead941e56020457b351c26bf; PPRD_P=UUID.1433937085-CT.138631.36.18; __wga=1587207386590.1587207255303.1586826184090.1586247616596.5.7; promotejs=dc9699088b486dcf38f886602ab91732a163RA',
    }

    params = (
        ('active', 'zhiboduihuanhb' + activeDate),
        ('level', '2'), # 1 20元红包、2 10元红包、3 5元红包、4 2元红包、5 1元红包
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
        hourTimestampFormat = time.strftime("%Y-%m-%d 00:00:00", time.localtime())
        hourTimestampArray = time.strptime(hourTimestampFormat, "%Y-%m-%d %H:%M:%S")
        hourTimestamp = int(time.mktime(hourTimestampArray) + 30)
        # 开始时间点
        startLoopPoint = time.strftime("%Y-%m-%d 23:59:55", time.localtime())
        startLoopPointArray = time.strptime(startLoopPoint, "%Y-%m-%d %H:%M:%S")
        startLoopPointTimestamp = int(time.mktime(startLoopPointArray))
        # print(startLoopPointTimestamp)
        # 当前时间在 T 23:59:55 --- T+1 00:00:30 之间
        if currentTimestamp < startLoopPointTimestamp or currentTimestamp > hourTimestamp:
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
