import requests
import time
import datetime
import json
import random

def collect_electric():
    t = time.time()
    microsecond = int(round(t * 1000))

    headers = {
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'zh-CN,zh;q=0.8',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Mobile Safari/537.36',
        'accept': '*/*',
        'referer': 'https://wqs.jd.com/pingou/dream_factory/index.html?share_ptag=1.1.1&jxsid=15907492306869524270&PTAG=17053.57.1&_fromplatform=jxapp&ad_od=share&utm_source=androidpingouapp&utm_medium=pingouappshare&utm_campaign=t_335139774&utm_term=CopyURL',
        'authority': 'wq.jd.com',
        'cookie': 'TrackID=1ifG5D4vHcNayBtaOgbVEbv1BUnQbAldtjDpwV9fx20xFW4pV3WGPzlq1iq-SLqJQA9BIgMf6lm0rE8TVNaTTcFI-t3IAgKEQo5rJcRIHmh0; pinId=p9q4GZ0bvhUviOw3JTn08g; unick=%E7%8C%AE%E6%B6%9B%E5%8B%87; _tp=%2BWZS%2FWDHCOCSXWgN63a%2BSw%3D%3D; _pst=754634469_m; user-key=b1844dcf-97b9-4cbc-b018-db5cfdccc6fb; cn=34; ipLoc-djd=15-1243-1244-42694; __jdu=15919692439311521756071; webp=1; sc_width=1536; visitkey=1400461977595702; wq_area=19_1607_4773%7C3; rurl=https%3A%2F%2Fwqs.jd.com%2Fpingou%2Fdream_factory%2Findex.html%3Fshare_ptag%3D1.1.1%26jxsid%3D15907492306869524270%26PTAG%3D17053.57.1%26_fromplatform%3Djxapp%26ad_od%3Dshare%26utm_source%3Dandroidpingouapp%26utm_medium%3Dpingouappshare%26utm_campaign%3Dt_335139774%26utm_term%3DCopyURL; shshshfpa=08cd40f0-2f51-44d4-1927-3ebc6e791092-1571148666; __jda=122270672.15919692439311521756071.1591969244.1592616032.1593252416.4; __jdb=122270672.3.15919692439311521756071|4.1593252416; __jdc=122270672; __jd_ref_cls=MLoginRegister_RiskCheck; mba_sid=15932524166307729402724242334.3; mba_muid=15919692439311521756071; TrackerID=IIjmzdZQ4lK74OmGPPZA9afwXPKMmhyzhgyzLNXjR0y4YpbJ6coMxB3wK_y682CTs1m5Ge5BcYX4Vkuu0n5F93kRCaQykOAEhMzUyUdYLYN_qeUbFmTCd2Xwf3NJyGQDnBu0O_s3WsV3vv78rkwyHg; pt_key=AAJe9xrDADA9J0zlJeMU6OIyWUUjRcrneKBG9LVnlV1UXbrdTkaCLEV3YJT-psrbxvWM54suNqY; pt_pin=jd_478f44263fce3; pt_token=vcmkzsh3; pwdt_id=jd_478f44263fce3; buy_uin=21620582635; jdpin=jd_478f44263fce3; pin=jd_478f44263fce3; wq_skey=zm60501BA263865E3CF7244A9698FF28BED02E014D8D1B021D95695C60480596227C8E868C5FBB22BAC23706C429EF27090174CFE7EAB5A5F0EEB001A0F087EDB2D74A7782C0D618A140CFF61ABB6B2D8B; wq_uin=21620582635; wxa_level=1; retina=1; cid=3; wqmnx1=MDEyNjM2MnR3LmlkZnl4P18xajE5NjdHMyZwcnBvcl9lb2cmZXBhcl9pMzdtPVI0OTdpLm5uIE41ZDhwSzdLIEcgZS45aWYzM2Y0ZkJLWUNGRigl; __wga=1593252547323.1593252414161.1592616029303.1592616029303.2.2; __jdv=76161171%7Candroidpingouapp%7Ct_335139774%7Cpingouappshare%7CCopyURL%7C1593252547329; _tj_rvurl=https%3A//wq.jd.com/cube/front/activePublish/dream_factory_report/380556.html%3Fshare_ptag%3D1.1.1%26jxsid%3D15907492306869524270%26PTAG%3D17053.57.1%26_fromplatform%3Djxapp%26ad_od%3Dshare%26utm_source%3Dandroidpingouapp%26utm_medium%3Dpingouappshare%26utm_campaign%3Dt_335139774%26utm_term%3DCopyURL; PPRD_P=UUID.15919692439311521756071-EA.17053.57.1; shshshfp=b4866c28a53301f3966dd04f8a84388c; shshshsID=6070f5be11a2b478b77ceaf320c5cc9c_4_1593252547812; shshshfpb=uYWOFkPYN%2FM%20B5N7rO9Iq9w%3D%3D; 3AB9D23F7A4B3C9B=HI7TLJCMD4CVOK4JEKNY6GUGCDELVN3E6FYYKSGA23YROC6NA4DBH6GXASNLAZUVVW66PCCWFNVQ72T4UZDBYFK6X4',
    }


    t2 = time.time()
    microsecond2 = int(round(t2 * 1000))
    params = (
        ('zone', 'dream_factory'),
        ('apptoken', ''),
        ('pgtimestamp', ''),
        ('phoneID', ''),
        ('factoryid', '3306240'),
        ('doubleflag', '0'),
        ('timeStamp', 'undefined'),
        ('_time', microsecond),
        ('_', microsecond2),
        ('g_login_type', '0'),
        ('callback', 'jsonpCBKQ'),
        ('g_tk', '603902029'),
        ('g_ty', 'ls'),
    )

    response = requests.get('https://wq.jd.com/dreamfactory/generator/CollectCurrentElectricity', headers=headers, params=params)
    localtime = time.asctime( time.localtime(time.time()) )
    print(response.text)

    # 根据返回结果处理
    resultText = response.text.replace('try {jsonpCBKQQ(', '')
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
