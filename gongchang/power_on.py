import requests
import time
import datetime

def invest_electric():
    t = time.time()
    microsecond = int(round(t * 1000))

    headers = {
        'authority': 'wq.jd.com',
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
        'accept': '*/*',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-dest': 'script',
        'referer': 'https://wqs.jd.com/pingou/dream_factory/index.html?ptag=138912.1.66&sceneval=2',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'webp=1; sc_width=1920; visitkey=28627513144879948; shshshfpa=f332fdcd-560b-5bf8-3c9c-9677b27ae4dc-1587518295; shshshfpb=cGa6CPa3nfOg4kZFPlxG7dg%3D%3D; retina=1; __jda=122270672.15881431483991546161782.1588143148.1588143148.1588143148.1; __jdc=122270672; areaId=19; TrackerID=01HToTouMIMHFimdWvPmTsZ1lCb3OidpxnSvQO6HXslr8ZVUBWde9X22QpgeJek-hz08SHp9x-_WetwMfHQDfaoFCcwGkBotAQomhc4YppVy2t8gJeaAVv70iQQXaQCS; pt_key=AAJeqXopADCSgr1TwFkDuwFeFmvdpC7IAmpkL0kQeJL1_95Baq2ioVCaJtRfDotT1SquqnhA3CI; pt_pin=754634469_m; pt_token=xjnpfv8x; pwdt_id=754634469_m; block_call_jdapp=11; wxa_level=1; sbx_hot_h=null; wq_addr=1472249671%7C19_1607_4773_62122%7C%u5E7F%u4E1C_%u6DF1%u5733%u5E02_%u5B9D%u5B89%u533A_%u897F%u4E61%u8857%u9053%7C%u5E7F%u4E1C%u6DF1%u5733%u5E02%u5B9D%u5B89%u533A%u897F%u4E61%u8857%u9053%u94F6%u7530%u8DEF4%u53F7%u667A%u8C37%u5B9D%u5B89%u667A%u8C37H%u5EA7609%7C113.859%2C22.5823; jdAddrId=19_1607_4773_62122; jdAddrName=%u5E7F%u4E1C_%u6DF1%u5733%u5E02_%u5B9D%u5B89%u533A_%u897F%u4E61%u8857%u9053; mitemAddrId=19_1607_4773_62122; mitemAddrName=%u5E7F%u4E1C%u6DF1%u5733%u5E02%u5B9D%u5B89%u533A%u897F%u4E61%u8857%u9053%u94F6%u7530%u8DEF4%u53F7%u667A%u8C37%u5B9D%u5B89%u667A%u8C37H%u5EA7609; wq_area=19_1607_4773%7C3; buy_uin=15432740016; jdpin=754634469_m; pin=754634469_m; wq_skey=zmB663C4BB8E5BC4E7C4BE572A3C37AA63A9BB06C243B0CE0FA9CEC902314205FFCC5D602572BFCD64466F49D97686D944B6D3A978BA3C9AF73EC7722E003160CA0AD168DDEF5E96D11B929FC017A42B2E; wq_uin=15432740016; __jdv=122270672%7Candroidpingouapp%7Ct_335139774%7Cpingouappshare%7CCopyURL%7C1588858835306; shshshfp=7ac63d776a6b9d82f2f20dbf5403a77d; cid=9; wqmnx1=MDEyNjM1MnQvam1ncmZyZHR0My4mZTI2MzdNbDBhUCAgIE8gZWk0NFRsRylzMU1lNSByNDhmN24yNDJZT09VIUgl; __wga=1588858886804.1588858238427.1588165058208.1587518294262.29.7; PPRD_P=UUID.15881431483991546161782-CT.138912.1.66-FOCUS.FO4O605%3ABOCEBAC3O57D714O76B34O2E363O23O1%3A018DE7688E0DBEF83O3BOF0041BO19O99O16O10066382CO76B3BOCEBAC5776A50EF3BD8419-EA.17053.57.1; _tj_rvurl=https%3A//wq.jd.com/cube/front/activePublish/dream_factory_report/380556.html%3Fptag%3D138912.1.66%26sceneval%3D2; shshshsID=ee1c11be35abdfe7829e8f6c1d45b2b7_29_1588858890044; 3AB9D23F7A4B3C9B=KNGXAJ5MPLC7DUADBMJVWLYDV5KT7G5KAO4YE33TEJXYBTAAAZELMQSCQLRHZSA4ZWKGWMCKWWXCJHXN2NXWEMAEQI',
    }

    params = (
        ('zone', 'dream_factory'),
        ('_time', microsecond),
        ('productionId', '1099515080572'),
        ('_', microsecond),
        ('sceneval', '2'),
        ('g_login_type', '1'),
        ('callback', 'jsonpCBKQ'),
        ('g_tk', '448376037'),
        ('g_ty', 'ls'),
    )

    response = requests.get('https://wq.jd.com/dreamfactory/userinfo/InvestElectric', headers=headers, params=params)
    localtime = time.asctime( time.localtime(time.time()) )

    # 根据返回结果处理
    resultText = response.text.replace('ry {jsonpCBKQ(', '')
    resultText = resultText.replace(')} catch (e) {}', '')
    # resultText = resultText.replace(';', '')
    resultTextJson = json.loads(resultText)
    if resultTextJson['msg'] == 'OK':
        print(localtime, '加电成功！')
    else:
        exit()

    print(localtime, '加电结果:', format(resultTextJson))

def cycle():
    """无规律的多次加电,防止被查出机器操作"""
    while True:
        invest_electric()
        time.sleep(600)

def main():
    # 调用
    cycle()
    
if __name__ == "__main__":
    main()
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://wq.jd.com/dreamfactory/userinfo/InvestElectric?zone=dream_factory&_time=1588858909667&productionId=1099515080572&_=1588858909668&sceneval=2&g_login_type=1&callback=jsonpCBKQ&g_tk=448376037&g_ty=ls', headers=headers)
