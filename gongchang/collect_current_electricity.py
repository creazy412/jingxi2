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
        'cookie': 'shshshfpa=490f7e17-1abe-d98b-e7ad-820b5f44f42f-1571622018; shshshfpb=khsT03U5oDfyZ%2FoU01w2Bfw%3D%3D; pinId=p9q4GZ0bvhUviOw3JTn08g; __jdu=1433937085; TrackID=1H6V0HWVPQH1CTcFqAalsPMA_2Yl6dGufZZX4pjjLKXbVyhbCwXEJDgDlvxINjb782x7OPHVMXmGjcinyVtp61E3oYjS7DgjtzNdfn8kT4Fo; pin=754634469_m; unick=%E7%8C%AE%E6%B6%9B%E5%8B%87; _tp=%2BWZS%2FWDHCOCSXWgN63a%2BSw%3D%3D; _pst=754634469_m; unpl=V2_ZzNtbUVVSxUgCkYBeE1aUWIFQQ8SBxASfFoTUHgaXlVnAkBUclRCFnQUR1NnGFwUZwcZX0JcRxRFCEdkeBpdA2QzIm1BV3MURQhDVnkRXgNmChZtclBDHEU4BBAkRwc1ZAoTWURVQBB3OEdkexFcDW4FF1lFVHNeGwkLVH4bXg1lBRNURmdBFXUIRGR4; areaId=15; cn=0; user-key=e6810f0e-d3cd-4b8b-b04a-88985d49c331; ipLoc-djd=15-1243-1244-42694; TrackerID=tsxj2_dZVqvLkjHT9VAa0jSn-IKkKfu7EKItUE9a6nagexkW4ZsvRlrdPAGiXCLRPVxDEAyxq5JzEjdtEfy2GJiuW6PIgrirjsPW8veps3E; pt_key=AAJe5bkoADDblCJMrueZBqqB1hUANAavP1pP-1iFV2HxmxH-418-VT8odyMJ2pKX1mT3up9jSX4; pt_pin=754634469_m; pt_token=q33quway; pwdt_id=754634469_m; wxa_level=1; cid=10; retina=1; webp=1; sc_width=1536; visitkey=68838765784605337; qd_uid=KBENM725-O3R289M7S6F60PMOHSIJ; qd_fs=1592114080827; sk_history=100007958788%2C100012122588%2C2429195%2C100003222943%2C; jxsid=15923984732003947137; __jdc=122270672; mobilev=html5; priceProPin=XOUEI5DK7NNXQ2RJYJSD7DJIN4; wq_logid=1592435074.1820540906; plusCustomBuryPointToken=1592438658961_4020; qd_ad=-%7C-%7Cdirect%7C-%7C0; qd_ls=1592432658748; qd_ts=1592439858370; qd_sq=16; wlfstk_smdl=qyym2ubxtjchjfgtiz6ni9llgc4hc622; __jda=122270672.1433937085.1565602967.1592442319.1592449252.95; __jdb=122270672.1.1433937085|95.1592449252; 3AB9D23F7A4B3C9B=HOENZJ47QVRFRK6WUOKPXZWRJX6DERJ4DJRRGLOXRJTI7NXJMCUYGHBIY54KEYZQ234HYRAQJLQ6DT6NPDPRA6BB4U; _tj_rvurl=https%3A//wq.jd.com/cube/front/activePublish/dream_factory_report/380556.html%3Fshare_ptag%3D1.1.1%26jxsid%3D15907492306869524270%26PTAG%3D17053.57.1%26_fromplatform%3Djxapp%26ad_od%3Dshare%26utm_source%3Dandroidpingouapp%26utm_medium%3Dpingouappshare%26utm_campaign%3Dt_335139774%26utm_term%3DCopyURL; PPRD_P=UUID.1433937085-LOGID.1592435074310.555423423-EA.17053.57.1; wq_area=19_1607_4773%7C3; buy_uin=15432740016; jdpin=754634469_m; wq_skey=zm5066B28EFFC94658B18C3D79F0E56AE2B2498936583AE00C31CEB4656660F07D12905B846EFB09C946D5B0E1681A670FB6D3A978BA3C9AF73EC7722E003160CA502374D12AC703560880484F7D48EF0B; wq_uin=15432740016; wqmnx1=MDEyNjM3MGgvLm5ldGRsXy5zMDYyRy5mdHhfcnNhcHBtcHAmbXQ5bUMyODZvNWhQbl9rT3BLLktsY3IwaTFhLi1zcjRhNFZVSEZI; __wga=1592449477984.1592449462696.1592435074297.1592113453477.3.19; __jdv=122270672%7Candroidpingouapp%7Ct_335139774%7Cpingouappshare%7CCopyURL%7C1592449477992; shshshfp=bb28c4616e6e3e83d8e4e812ae8a4ea1; shshshsID=08c295a7a83c68c2e08ebe31a88f96c1_4_1592449478406',
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
        ('callback', 'jsonpCBKHHH'),
        ('g_tk', '974267104'),
        ('g_ty', 'ls'),
    )

    response = requests.get('https://wq.jd.com/dreamfactory/generator/CollectCurrentElectricity', headers=headers, params=params)
    localtime = time.asctime( time.localtime(time.time()) )
    print(response.text)

    # 根据返回结果处理
    resultText = response.text.replace('try {jsonpCBKHHH(', '')
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
