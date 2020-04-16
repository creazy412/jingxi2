import requests
import time
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import sys

def exchange():
    t = time.time()
    microsecond = int(round(t * 1000))
    activeDate = time.strftime("%Y%#m%d", time.localtime())

    headers = {
        'authority': 'wq.jd.com',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36',
        'sec-fetch-dest': 'script',
        'accept': '*/*',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'no-cors',
        'referer': 'https://wqs.jd.com/pglive/task/index.html?sceneval=2',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'shshshfpa=490f7e17-1abe-d98b-e7ad-820b5f44f42f-1571622018; shshshfpb=khsT03U5oDfyZ%2FoU01w2Bfw%3D%3D; pinId=p9q4GZ0bvhUviOw3JTn08g; __jdu=1433937085; unpl=V2_ZzNtbUsHRBZzXRUEfhlUBWJTFw4RAkRGdgpBUSlOWwJjBUZdclRCFnQUR1ZnGVoUZwQZWUtcQRJFCEFkfxtfDGADEFRyZ3MWdThHZHscXgdvARRcS1NzJXIIT2R7GloGbgIUXHIEE0ojWxYLLUYZNWYzE21DZxF7rb7wjN6oQNHNjMfV1RpDEHcKTlZ9GFUBVwIiXg%3d%3d; __jdv=76161171%7Cbaidu%7C-%7Corganic%7Cnot%20set%7C1586093544852; areaId=19; ipLoc-djd=19-1607-0-0; TrackID=1H6V0HWVPQH1CTcFqAalsPMA_2Yl6dGufZZX4pjjLKXbVyhbCwXEJDgDlvxINjb782x7OPHVMXmGjcinyVtp61E3oYjS7DgjtzNdfn8kT4Fo; pin=754634469_m; unick=%E7%8C%AE%E6%B6%9B%E5%8B%87; _tp=%2BWZS%2FWDHCOCSXWgN63a%2BSw%3D%3D; _pst=754634469_m; __jda=76161171.1433937085.1565602967.1586224508.1586246687.26; __jdc=76161171; webp=1; visitkey=43179755944294334; sc_width=400; block_call_jdapp=11; 3AB9D23F7A4B3C9B=UHLJPPNJYGNUTGKGPQXUX57EJ4ZH2RY725YSYIBMXHRXKS2L3PEIWIRWDYNB3FNKX6MZQHMUWVI232ZXYIKIYB3H34; retina=1; wxa_level=1; TrackerID=77OnRyyhaIxQ6YgCV3-Q6x3OD1Mnxzrmxh1J_oWlpaqTB8mGnO_Fea_5b_GEdh-F58yWSt2YVtol24vYKDOtX3Z8bvA3u6tLqi0MX20XDZ2dcM0kLUZwSHex3nnbg9S0auQAD4E8Ojub9nrTRWyKyw; pt_key=AAJelGk-ADATQxnhjDbBnBf7DaZRy0U6kA87pIredOWl35SUOFU42iVXrPECT4BAFu5NC3aywVw; pt_pin=jd_478f44263fce3; pt_token=n4zk9w5j; pwdt_id=jd_478f44263fce3; cid=9; shshshfp=63dc7904ead941e56020457b351c26bf; PPRD_P=UUID.1433937085-CT.138631.36.18; wqmnx1=MDEyNjM2MGgvai9lLy5zYTQ1OW8vTCBpO3NpQUFlNSBMZW9vLjdNIGkzM2ZmMjVWRUlVKFI%3D; __wga=1586826184090.1586826184090.1586784387455.1586247616596.1.6; shshshsID=856688795197fedb2239de24317bafd6_1_1586826184573; promotejs=6afcb4268dabed340d3ff7c6e21831cbab1212cd',
    }

    params = (
        ('active', 'zhiboduihuanhb' + activeDate),
        # ('active', 'zhiboduihuanhb2020414'),
        ('level', '1'), # 1 20 元的优惠券
        ('platform', '4'),
        ('_', microsecond),
        ('sceneval', '2'),
        ('g_login_type', '1'),
        ('callback', 'jsonpCBKL'),
        ('g_ty', 'ls'),
    )

    response = requests.get('https://wq.jd.com/jxlivetask/DrawAward', headers=headers, params=params)
    localtime = time.asctime( time.localtime(time.time()) )

    print(localtime, '兑换结果:', response.text)

def cycle():
    """
    循环调用
    如果当前时间大于整点+1分额时候 continue
    """

    while True:
        currentTimestamp = int(time.time())
        hourTimestampFormat = time.strftime("%Y-%m-%d %H:00:00", time.localtime())
        hourTimestampArray = time.strptime(hourTimestampFormat, "%Y-%m-%d %H:%M:%S")
        # print(hourTimestampArray)
        hourTimestamp = int(time.mktime(hourTimestampArray) + 60)
        if currentTimestamp > hourTimestamp:
            # print('currentTimestamp ', currentTimestamp)
            # print(hourTimestamp)
            # print('continue', loopCounter)
            # loopCounter += 1
            continue
        exchange()
        time.sleep(1)

# startDate = time.strftime("%Y-%m-%d", time.localtime()) + ' 23:58:00'

# def main():
# 创建调度器：BlockingScheduler
# scheduler = BlockingScheduler()
# # 定时脚本任务
# scheduler.add_job(cycle, 'date', run_date = startDate)
# scheduler.start()

# 调试
cycle()
    

# if __name__ == "__main__":
#     main()
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://wq.jd.com/jxlivetask/DrawAward?active=zhiboduihuanhb2020412&level=1&platform=4&_=1586652179175&sceneval=2&g_login_type=1&callback=jsonpCBKM&g_ty=ls', headers=headers, cookies=cookies)
