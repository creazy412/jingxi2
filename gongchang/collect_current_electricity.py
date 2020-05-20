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
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
        'accept': '*/*',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-dest': 'script',
        'referer': 'https://wqs.jd.com/pingou/dream_factory/index.html?ptag=138912.1.66&sceneval=2&jxsid=15899826033739777668',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'webp=1; sc_width=1920; visitkey=28627513144879948; shshshfpa=f332fdcd-560b-5bf8-3c9c-9677b27ae4dc-1587518295; shshshfpb=cGa6CPa3nfOg4kZFPlxG7dg%3D%3D; retina=1; __jda=122270672.15881431483991546161782.1588143148.1588143148.1588143148.1; TrackerID=01HToTouMIMHFimdWvPmTsZ1lCb3OidpxnSvQO6HXslr8ZVUBWde9X22QpgeJek-hz08SHp9x-_WetwMfHQDfaoFCcwGkBotAQomhc4YppVy2t8gJeaAVv70iQQXaQCS; pt_key=AAJeqXopADCSgr1TwFkDuwFeFmvdpC7IAmpkL0kQeJL1_95Baq2ioVCaJtRfDotT1SquqnhA3CI; pt_pin=754634469_m; pt_token=xjnpfv8x; pwdt_id=754634469_m; sbx_hot_h=null; wq_addr=1472249671%7C19_1607_4773_62122%7C%u5E7F%u4E1C_%u6DF1%u5733%u5E02_%u5B9D%u5B89%u533A_%u897F%u4E61%u8857%u9053%7C%u5E7F%u4E1C%u6DF1%u5733%u5E02%u5B9D%u5B89%u533A%u897F%u4E61%u8857%u9053%u94F6%u7530%u8DEF4%u53F7%u667A%u8C37%u5B9D%u5B89%u667A%u8C37H%u5EA7609%7C113.859%2C22.5823; jdAddrId=19_1607_4773_62122; jdAddrName=%u5E7F%u4E1C_%u6DF1%u5733%u5E02_%u5B9D%u5B89%u533A_%u897F%u4E61%u8857%u9053; mitemAddrId=19_1607_4773_62122; mitemAddrName=%u5E7F%u4E1C%u6DF1%u5733%u5E02%u5B9D%u5B89%u533A%u897F%u4E61%u8857%u9053%u94F6%u7530%u8DEF4%u53F7%u667A%u8C37%u5B9D%u5B89%u667A%u8C37H%u5EA7609; wxa_level=1; jxsid=15899826033739777668; wq_area=19_1607_4773%7C3; buy_uin=15432740016; jdpin=754634469_m; pin=754634469_m; wq_skey=zm5DC4A838D74FE89F217501C245F00394E1BBCBF1D6674148CD3CEA5B31A60E1CBF22362445D6B39211670B285A9EF5A2B6D3A978BA3C9AF73EC7722E003160CABD90C0023C52C2A096158258A7BD7357; wq_uin=15432740016; __jdv=122270672%7Candroidpingouapp%7Ct_335139774%7Cpingouappshare%7CCopyURL%7C1589982607980; shshshfp=7ac63d776a6b9d82f2f20dbf5403a77d; cid=9; wqmnx1=MDEyNjM4Ny9jb18vdD0xbmo4MzYyOHowIDFlIGU2ICBjczAvZi84ZlUyVk8pKCk%3D; __wga=1589982658452.1589982604002.1588898481788.1587518294262.4.9; PPRD_P=UUID.15881431483991546161782-EA.17053.57.1-CT.138912.1.66; _tj_rvurl=https%3A//wq.jd.com/cube/front/activePublish/dream_factory_report/380556.html%3Fptag%3D138912.1.66%26sceneval%3D2%26jxsid%3D15899826033739777668; shshshsID=70939981a23e0e9c5e0d779f5e0a06f0_4_1589982660283; 3AB9D23F7A4B3C9B=KNGXAJ5MPLC7DUADBMJVWLYDV5KT7G5KAO4YE33TEJXYBTAAAZELMQSCQLRHZSA4ZWKGWMCKWWXCJHXN2NXWEMAEQI',
    }

    t2 = time.time()
    microsecond2 = int(round(t2 * 1000))
    params = (
        ('zone', 'dream_factory'),
        ('factoryid', '1099513774545'),
        ('doubleflag', '0'),
        ('timeStamp', 'undefined'),
        ('_time', microsecond),
        ('_', microsecond2),
        ('sceneval', '2'),
        ('g_login_type', '1'),
        ('callback', 'jsonpCBKX'),
        ('g_tk', '447946603'),
        ('g_ty', 'ls'),
    )

    response = requests.get('https://wq.jd.com/dreamfactory/generator/CollectCurrentElectricity', headers=headers, params=params)
    localtime = time.asctime( time.localtime(time.time()) )
    print(response.text)

    # 根据返回结果处理
    resultText = response.text.replace('try {jsonpCBKX(', '')
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
        startLoopPoint = time.strftime("%Y-%m-%d 00:30:49", time.localtime())
        startLoopPointArray = time.strptime(startLoopPoint, "%Y-%m-%d %H:%M:%S")
        startLoopPointTimestamp = int(time.mktime(startLoopPointArray))
        # 结束时间点
        stopLoopPointTimestamp = startLoopPointTimestamp + (5 * 60 * 3600)

        if currentTimestamp > startLoopPointTimestamp and currentTimestamp < stopLoopPointTimestamp:
            continue
            
        collect_electric()
        sleep_time = random.randint(200,300)
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
