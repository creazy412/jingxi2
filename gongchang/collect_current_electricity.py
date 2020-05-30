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
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Mobile Safari/537.36',
        'accept': '*/*',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-dest': 'script',
        'referer': 'https://wqs.jd.com/pingou/dream_factory/index.html?share_ptag=1.1.1&jxsid=15907492306869524270&PTAG=17053.57.1&_fromplatform=jxapp&ad_od=share&utm_source=androidpingouapp&utm_medium=pingouappshare&utm_campaign=t_335139774&utm_term=CopyURL',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '__jdu=15510555295861266323195; shshshfpa=35670fbc-6fb1-0e99-5b6c-1d92b073e604-1551055531; shshshfpb=kkDG3ocAfgjv1kYR55cL6GQ%3D%3D; webp=1; visitkey=20405373257032906; __jda=122270672.15510555295861266323195.1551055530.1583414707.1589696846.6; ipLoc-djd=15-1243-1244-42694; wxa_level=1; cid=3; _tj_rvurl=https%3A//wq.jd.com/cube/front/activePublish/dream_factory_report/380556.html%3Fshare_ptag%3D1.1.1%26jxsid%3D15907492306869524270%26PTAG%3D17053.57.1%26_fromplatform%3Djxapp%26ad_od%3Dshare%26utm_source%3Dandroidpingouapp%26utm_medium%3Dpingouappshare%26utm_campaign%3Dt_335139774%26utm_term%3DCopyURL; PPRD_P=UUID.15510555295861266323195-EA.17053.57.1; sc_width=1536; wq_area=15_1243_0%7C3; rurl=https%3A%2F%2Fwqs.jd.com%2Fpingou%2Fdream_factory%2Findex.html%3Fshare_ptag%3D1.1.1%26jxsid%3D15907492306869524270%26PTAG%3D17053.57.1%26_fromplatform%3Djxapp%26ad_od%3Dshare%26utm_source%3Dandroidpingouapp%26utm_medium%3Dpingouappshare%26utm_campaign%3Dt_335139774%26utm_term%3DCopyURL; TrackerID=adlE5F2h2lwIeIisSm_z6qCelRvMRnHoLWG4MXKSGDPlQCvF8cu1gI3Y4PZWa7JIUg7A3MV7siOUzRbZ00l-cArN80eKxvXRG17v1LTjo3lr_EW0ukcNNkmTjQTMjc9J; pt_key=AAJe0dHvADDo7S_ku4IWtjX-BQsFu3IcuvEy26mwlFIPaBlCt4gRX7f5wjyjaBUQxh82ZpYfYsg; pt_pin=754634469_m; pt_token=8izsaw17; pwdt_id=754634469_m; buy_uin=15432740016; jdpin=754634469_m; pin=754634469_m; wq_skey=zm6CF9389C99518F64360ED290F4338F3DF397FF717CAC72F9A826913D107A9DC7BE17E58A738E675A5E8DE560D80A7D5DB6D3A978BA3C9AF73EC7722E003160CA9F718E249AD785EF02142D4AE5011974; wq_uin=15432740016; retina=1; shshshfp=7194102934210c2850341a0f1c1937a7; 3AB9D23F7A4B3C9B=LTLK77KD7ALLHMCCMKOG5GPB2NDBKRJQ4H4A5VQCYLSQ5TSO5MNWY6RAP3II2XCB3SPNCSJSFHMHR74F7V57IBYPOI; wqmnx1=MDEyNjM4NTpkbmFyLmE9eDA4MDcxbGpfZXVyb209cHVhMyZtTDUzaSAgIHhpOGU1S2lvZTBvZi5GNC0zWVMqKA%3D%3D; __wga=1590809806085.1590809026586.1586787092484.1583414565242.4.5; __jdv=122270672%7Candroidpingouapp%7Ct_335139774%7Cpingouappshare%7CCopyURL%7C1590809806091; shshshsID=a9443b8419d57769497e456c6232ea10_5_1590809806479',
    }

    t2 = time.time()
    microsecond2 = int(round(t2 * 1000))
    params = (
        ('zone', 'dream_factory'),
        ('apptoken', ''),
        ('pgtimestamp', ''),
        ('phoneID', ''),
        ('factoryid', '1099513774545'),
        ('doubleflag', '0'),
        ('timeStamp', 'undefined'),
        ('_time', microsecond),
        ('_', microsecond2),
        ('g_login_type', '0'),
        ('callback', 'jsonpCBKR'),
        ('g_tk', '584444182'),
        ('g_ty', 'ls'),
    )

    response = requests.get('https://wq.jd.com/dreamfactory/generator/CollectCurrentElectricity', headers=headers, params=params)
    localtime = time.asctime( time.localtime(time.time()) )
    print(response.text)

    # 根据返回结果处理
    resultText = response.text.replace('try {jsonpCBKR(', '')
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
