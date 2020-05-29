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
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'sec-fetch-dest': 'script',
        'accept': '*/*',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'no-cors',
        'referer': 'https://wqs.jd.com/pingou/dream_factory/index.html?share_ptag=1.1.1&jxsid=15907492306869524270&PTAG=17053.57.1&_fromplatform=jxapp&ad_od=share&utm_source=androidpingouapp&utm_medium=pingouappshare&utm_campaign=t_335139774&utm_term=CopyURL',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'shshshfpa=490f7e17-1abe-d98b-e7ad-820b5f44f42f-1571622018; shshshfpb=khsT03U5oDfyZ%2FoU01w2Bfw%3D%3D; pinId=p9q4GZ0bvhUviOw3JTn08g; __jdu=1433937085; TrackID=1H6V0HWVPQH1CTcFqAalsPMA_2Yl6dGufZZX4pjjLKXbVyhbCwXEJDgDlvxINjb782x7OPHVMXmGjcinyVtp61E3oYjS7DgjtzNdfn8kT4Fo; user-key=c0a987f2-6776-4e56-a23c-e12f1e5331b5; cn=2; __jda=122270672.1433937085.1565602967.1588509394.1590669227.28; __jdc=122270672; areaId=19; ipLoc-djd=19-1607-4773-0; 3AB9D23F7A4B3C9B=HOENZJ47QVRFRK6WUOKPXZWRJX6DERJ4DJRRGLOXRJTI7NXJMCUYGHBIY54KEYZQ234HYRAQJLQ6DT6NPDPRA6BB4U; wxa_level=1; retina=1; cid=3; webp=1; sc_width=1536; wq_area=19_1607_4773%7C3; rurl=https%3A%2F%2Fwqs.jd.com%2Fpingou%2Fdream_factory%2Findex.html%3Fshare_ptag%3D1.1.1%26jxsid%3D15907492306869524270%26PTAG%3D17053.57.1%26_fromplatform%3Djxapp%26ad_od%3Dshare%26utm_source%3Dandroidpingouapp%26utm_medium%3Dpingouappshare%26utm_campaign%3Dt_335139774%26utm_term%3DCopyURL; TrackerID=xibJX-2qEsgmtuYUf8mKF5-2NSUzhKSlfsU0NqCQN8a5xucdEsEXzwQVaYs0jQlm2GDsHqYhmU2-pq-UVit_3scqUw6X4TdFMrfZYiqSa05UIgJk8FdfbkoAZNtxNigbMATQRMMGgpuZCVsAWqbAzg; pt_key=AAJe0OkkADCmGV6ULGx5E6DeNxuJgEfy8YyMtk3LrlMWRftYUh_XFk2_xcUC7oNYQortQ6m3Gr8; pt_pin=jd_478f44263fce3; pt_token=9wyop8ok; pwdt_id=jd_478f44263fce3; buy_uin=21620582635; jdpin=jd_478f44263fce3; pin=jd_478f44263fce3; wq_skey=zm66F0EF2BB5A7615DDA1AC1829FC572E923BFA271287DCAF1FD10163506A1450EB2010EFD4349A64B75A7D308C67CA98F34427D74EA9B25F00237998BBA048090D7982602B71A2597CE2331333FF370917FA9085E92B511C7B35B054AB64DDE0A; wq_uin=21620582635; wqmnx1=MDEyNjM5Ny9vL2NlaD1zNDVBNW09XyZjZHBpdSZhNXRvTS5laDNlWGUuVCBlLmwgMEZkLTJVKSY%3D; __wga=1590749478280.1590749350164.1590749350164.1590749350164.2.1; __jdv=76161171%7Candroidpingouapp%7Ct_335139774%7Cpingouappshare%7CCopyURL%7C1590749478287; shshshfp=bb28c4616e6e3e83d8e4e812ae8a4ea1; shshshsID=e778652691e786b70c1e3544b0de2ead_3_1590749478680; visitkey=68838765784605337; _tj_rvurl=https%3A//wq.jd.com/cube/front/activePublish/dream_factory_report/380556.html%3Fshare_ptag%3D1.1.1%26jxsid%3D15907492306869524270%26PTAG%3D17053.57.1%26_fromplatform%3Djxapp%26ad_od%3Dshare%26utm_source%3Dandroidpingouapp%26utm_medium%3Dpingouappshare%26utm_campaign%3Dt_335139774%26utm_term%3DCopyURL; PPRD_P=UUID.1433937085-EA.17053.57.1',
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
        ('callback', 'jsonpCBKP'),
        ('g_tk', '810636292'),
        ('g_ty', 'ls'),
    )

    response = requests.get('https://wq.jd.com/dreamfactory/generator/CollectCurrentElectricity', headers=headers, params=params)
    localtime = time.asctime( time.localtime(time.time()) )
    print(response.text)

    # 根据返回结果处理
    resultText = response.text.replace('try {jsonpCBKP(', '')
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
