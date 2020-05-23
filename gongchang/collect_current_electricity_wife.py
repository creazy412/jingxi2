import requests
import time
import datetime
import json
import random

def collect_electric():
    t = time.time()
    microsecond = int(round(t * 1000))

    headers = {
        'authority': 'wq.jd.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'accept': '*/*',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-dest': 'script',
        'referer': 'https://wqs.jd.com/pingou/dream_factory/index.html?share_ptag=1.1.1&jxsid=15902028949811582480&PTAG=17053.57.1&_fromplatform=jxapp&ad_od=share&utm_source=androidpingouapp&utm_medium=pingouappshare&utm_campaign=t_335139774&utm_term=CopyURL',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '__jdu=1589984592067854966288; 3AB9D23F7A4B3C9B=ZJB2J3YFRYGTLIRTEHG6SVLYHZHNUUKLVDWFM252ROKFFG7PCA2AJFZU3B7QOBIUOUZJP43PLUO7WUIHVUOZFW5G3Q; pinId=p9q4GZ0bvhUviOw3JTn08g; unick=%E7%8C%AE%E6%B6%9B%E5%8B%87; _tp=%2BWZS%2FWDHCOCSXWgN63a%2BSw%3D%3D; _pst=754634469_m; TrackID=1WIDrOcd4czpv5wNL5oyECQhYUCZ2irsS_BRGqhqBz7DaMTptSRFug19fd3inoGVbGNzsxyI98Y9Um0a7rh9sqDz-SDrqq9LRcj3ayyvK-7g; wxa_level=1; retina=0; cid=3; webp=1; sc_width=1536; wq_area=15_1213_0%7C3; visitkey=10913513581653556; PPRD_P=UUID.1589984592067854966288-EA.17053.57.1; shshshfpa=6549d940-e666-8194-e497-909ec30a88c4-1590202973; __jda=122270672.1589984592067854966288.1589984592.1590118760.1590202974.3; mba_muid=1589984592067854966288; shshshfpb=of%202NC3JqmU%20oH38eBcm4AA%3D%3D; _tj_rvurl=https%3A//wq.jd.com/cube/front/activePublish/dream_factory_report/380556.html%3Fshare_ptag%3D1.1.1%26jxsid%3D15902028949811582480%26PTAG%3D17053.57.1%26_fromplatform%3Djxapp%26ad_od%3Dshare%26utm_source%3Dandroidpingouapp%26utm_medium%3Dpingouappshare%26utm_campaign%3Dt_335139774%26utm_term%3DCopyURL; rurl=https%3A%2F%2Fwqs.jd.com%2Fpingou%2Fdream_factory%2Findex.html%3Fshare_ptag%3D1.1.1%26jxsid%3D15902028949811582480%26PTAG%3D17053.57.1%26_fromplatform%3Djxapp%26ad_od%3Dshare%26utm_source%3Dandroidpingouapp%26utm_medium%3Dpingouappshare%26utm_campaign%3Dt_335139774%26utm_term%3DCopyURL; __jdc=122270672; __jdb=122270672.4.1589984592067854966288|3.1590202974; mba_sid=15902029746974085701146825364.4; __jd_ref_cls=MLoginRegister_RiskCheck; pwdt_id=jd_478f44263fce3; pt_token=s23xndda; pt_pin=jd_478f44263fce3; pt_key=AAJeyJMKADCVjMq5P52EUt58i2ZYB7OsxwaD0qhUUAP6dLopLy3Vzb_qhCTsq-8fJJIRShqUjZo; TrackerID=jfiBjViqqw7kCBKUlS8EUF9OYd89N7T5_JNUBaPy_J3BRy6RkJMxOq2KpdaVSyiz4KPi-OpiHISp4SliZh8ciUSI2522I6nppmikSBIb7EE; buy_uin=21620582635; jdpin=jd_478f44263fce3; pin=jd_478f44263fce3; wq_skey=zm66F0EF2BB5A7615DDA1AC1829FC572E905BAA4F939D457E7D1684CD92C250E5F6CC84D3B2B963A4F3E4E79460D735753606E3D2CEE78908F038FCAC6E8F9B798DB0F37E98A9CCE4D6405699315C3BB74D65A55358630D58318BC48C4A2C270D3; wq_uin=21620582635; wqmnx1=MDEyNjM2MGgvai91bW9kbXJnMWQyOTJUMC5vZnhkaHRyZGlwX21vaHRwdDN1cnk4NTZNYSh3Nml4cGIzKCwgKW0wLmE1MXI3VTQ0V09ISCkp; __wga=1590203148331.1590202971653.1590202971653.1590202971653.4.1; __jdv=122270672%7Candroidpingouapp%7Ct_335139774%7Cpingouappshare%7CCopyURL%7C1590203148339; shshshfp=2c96af94ca172aff0718ae4bd6be1fe1; shshshsID=ae89dab343f40443e7159f8f764c31f2_7_1590203149382',
    }

    t2 = time.time()
    microsecond2 = int(round(t2 * 1000))
    params = (
        ('zone', 'dream_factory'),
        ('factoryid', '3306240'),
        ('doubleflag', '0'),
        ('timeStamp', 'undefined'),
        ('_time', microsecond),
        ('_', microsecond2),
        ('g_login_type', '0'),
        ('callback', 'jsonpCBKNN'),
        ('g_tk', '646613014'),
        ('g_ty', 'ls'),
    )

    response = requests.get('https://wq.jd.com/dreamfactory/generator/CollectCurrentElectricity', headers=headers, params=params)
    localtime = time.asctime( time.localtime(time.time()) )
    print(response.text)

    # 根据返回结果处理
    resultText = response.text.replace('try {jsonpCBKNN(', '')
    resultText = resultText.replace(')} catch (e) {}', '')
    # resultText = resultText.replace(';', '')
    resultTextJson = json.loads(resultText)
    if resultTextJson['msg'] == 'OK':
        print(localtime, '收电成功！')
    else:
        exit()

    print(localtime, '收电结果:', format(resultTextJson))

def cycle():
    """无规律的多次加电,防止被查出机器操作"""
    while True:
        currentTimestamp = int(time.time())
        # 开始时间点
        startLoopPoint = time.strftime("%Y-%m-%d 00:00:00", time.localtime())
        startLoopPointArray = time.strptime(startLoopPoint, "%Y-%m-%d %H:%M:%S")
        startLoopPointTimestamp = int(time.mktime(startLoopPointArray))
        # 结束时间点
        stopLoopPointTimestamp = startLoopPointTimestamp + (6 * 3600) + 60
        # print(startLoopPointTimestamp)
        # print(stopLoopPointTimestamp)
        if currentTimestamp > startLoopPointTimestamp and currentTimestamp < stopLoopPointTimestamp:
            continue
        else:
            collect_electric()
            sleep_time = random.randint(200,1500)
            # sleep_time = 5
            time.sleep(sleep_time)

def main():
    # 调用
    cycle()
    
if __name__ == "__main__":
    main()
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://wq.jd.com/dreamfactory/userinfo/InvestElectric?zone=dream_factory&_time=1588858909667&productionId=1099515080572&_=1588858909668&sceneval=2&g_login_type=1&callback=jsonpCBKQ&g_tk=448376037&g_ty=ls', headers=headers)
