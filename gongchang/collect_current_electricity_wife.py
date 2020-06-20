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
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
        'accept': '*/*',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-dest': 'script',
        'referer': 'https://wqs.jd.com/pingou/dream_factory/index.html?share_ptag=1.1.1&jxsid=15902028949811582480&PTAG=17053.57.1&_fromplatform=jxapp&ad_od=share&utm_source=androidpingouapp&utm_medium=pingouappshare&utm_campaign=t_335139774&utm_term=CopyURL',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '__jdu=1589984592067854966288; shshshfpa=6549d940-e666-8194-e497-909ec30a88c4-1590202973; shshshfpb=of%202NC3JqmU%20oH38eBcm4AA%3D%3D; areaId=15; ipLoc-djd=15-1213-0-0; TrackID=1mYJZaiN7buvpVR7Dy14bmKu-ktSXscwy_gheqjrtxzcxBM9Q1JU42JsARsyeyjn6Zw8JvafbQuMwhZdUgIqrcyEdI5ir7e2LYOx5KkjginJymEiePxeUAyRBLgR0m0VS; thor=8588A18ED190ADDD1EBBD96A198619288C15D4CAA8BC4C88EADCBBD4B6CA4CAA2BE8843E48E7C0DFF2D72E9C90EAAA141528393EC0AF618214C12BD6E454258D1BA39D5DA10EBF9407764BE7805DF192F676E4CD0AC25B388E569DB4A7E2BB88131DFA37C00DBA96B748A0F48AF4CDD0AB36E3C6E04BFED9D55919CC12CF17A90C9D823C83929A5798DFC99D57BFCA0B229EBCAE5EA2CAD460922E230F47231C; pinId=GhBdgvO0uLXmaS3Wxf6NPLV9-x-f3wj7; unick=jd_186820yeq; ceshi3.com=201; _tp=uMxD0se7sdZuxkPMSTgBZxGR2F9gI0KP09M6ADvi5Xo%3D; _pst=jd_478f44263fce3; pin=jd_478f44263fce3; __jdc=76161171; rurl=https%3A%2F%2Fwqs.jd.com%2Fpingou%2Fdream_factory%2Findex.html%3Fshare_ptag%3D1.1.1%26jxsid%3D15902028949811582480%26PTAG%3D17053.57.1%26_fromplatform%3Djxapp%26ad_od%3Dshare%26utm_source%3Dandroidpingouapp%26utm_medium%3Dpingouappshare%26utm_campaign%3Dt_335139774%26utm_term%3DCopyURL; mba_muid=1589984592067854966288; 3AB9D23F7A4B3C9B=ZJB2J3YFRYGTLIRTEHG6SVLYHZHNUUKLVDWFM252ROKFFG7PCA2AJFZU3B7QOBIUOUZJP43PLUO7WUIHVUOZFW5G3Q; __jda=76161171.1589984592067854966288.1589984592.1592615779.1592634383.7; pwdt_id=jd_478f44263fce3; pt_token=0qpyhu23; pt_pin=jd_478f44263fce3; pt_key=AAJe7ayyADBmJbLlfhnAd66qE3oCyoFp6pc3hdFHQBi1ajq6I5on_C88DT5DpATgOoqrAHM7E2Y; TrackerID=huP-z0-XteAgM9v229raGaLAJoMQbS_hOZUSGc3ezxb1tkTHQYRmIXblAqiRiMhY0rRXGLkOp3dCQnPc58q2OJuvaBdIG2kvI9qSmSjEPBuetMHna-NgdJOCFn_6BDY1; __jd_ref_cls=MLoginRegister_SMSLoginSuccess; buy_uin=21620582635; jdpin=jd_478f44263fce3; wq_skey=zm04054EF3127BB7DB17DD04FC5C2E5952D6296DB9E04C1A6D97F9FB813F6697777719C7C82814D3E3C5F99FFD4D4DFB4C34427D74EA9B25F00237998BBA0480904D096D6B174EEBDF03066FDC301D591684BC820AF069041AD0B19B7C21176B6E; wq_uin=21620582635; wxa_level=1; retina=1; cid=3; webp=1; sc_width=1536; wq_area=15_1213_0%7C3; visitkey=10913513581653556; PPRD_P=UUID.1589984592067854966288-EA.17053.57.1; wqmnx1=MDEyNjM1NHNxLnB1YWMveGxyYTF4MTA5OCY9MzFvdD1wb2F0dWFpZ3BfdW5wcm1wPTU3bW15MzE1M29hIHVuZDt1Qi84cGUvM0ggIG9yODQxbyByNzNyMmYtMktXVUkjJigp; __wga=1592637091644.1592637091644.1592634550196.1592634550196.1.2; __jdv=122270672%7Candroidpingouapp%7Ct_335139774%7Cpingouappshare%7CCopyURL%7C1592637091653; _tj_rvurl=https%3A//wq.jd.com/cube/front/activePublish/dream_factory_report/380556.html%3Fshare_ptag%3D1.1.1%26jxsid%3D15902028949811582480%26PTAG%3D17053.57.1%26_fromplatform%3Djxapp%26ad_od%3Dshare%26utm_source%3Dandroidpingouapp%26utm_medium%3Dpingouappshare%26utm_campaign%3Dt_335139774%26utm_term%3DCopyURL; shshshfp=7ed7f90cb117c645fe48d5c83cf6b6fb; shshshsID=4b44cb95ecd1a0136a0a8fd2b7c3d3f3_1_1592637095367',
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
        ('callback', 'jsonpCBKQQ'),
        ('g_tk', '504778450'),
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
