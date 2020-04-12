import requests

cookies = {
    '__jdu': '15510555295861266323195',
    'shshshfpa': '35670fbc-6fb1-0e99-5b6c-1d92b073e604-1551055531',
    'shshshfpb': 'kkDG3ocAfgjv1kYR55cL6GQ%3D%3D',
    '3AB9D23F7A4B3C9B': 'YAZYEV2VJOD6QJZM7WBS3G7ATMRXMBWGI6TCSUILAI3AQVTIJJWK7G4MZU3HILXX3ZRGORRWNL6KDUCX45I3SLIVGM',
    'webp': '1',
    'visitkey': '20405373257032906',
    '__jda': '122270672.15510555295861266323195.1551055530.1578145679.1583414707.5',
    'wxa_level': '1',
    'block_call_jdapp': '11',
    '__jdv': '122270672%7Cbaidu%7C-%7Corganic%7Cnot%20set%7C1586649190834',
    'sc_width': '1536',
    'wq_area': '53283_53440_0%7C0',
    'TrackerID': '0tHcRgNngOnNGDBkK-5FrIAdu6cXCI6eD3GNZ_-AFH8w8Onp-EBRU-dp-31ThJmTmuZsHug8Jc40TuUAsfCo1xfYQItcMbFg_Jz77Tdsh3lJHHEhuL5Rkb3q_e4zDLwD',
    'pt_key': 'AAJekloaADCA6o9CfSSn-lEonQds5nngGCVfgiFZ7RnhqN2BfHuqwvL0qxrze_AYKV_FQ0NRU1Y',
    'pt_pin': '754634469_m',
    'pt_token': '838vz8v3',
    'pwdt_id': '754634469_m',
    'retina': '1',
    'cid': '9',
    'PPRD_P': 'UUID.15510555295861266323195-FOCUS.FO4O305%3ABOCE2543O575AA4O76DB4O2DBE3O23O1%3AFOFO9O17O1FOFO6382CO76DBBOCE2547C01A30CE2CE0627-CT.138631.36.18',
    'shshshfp': '09ee4b5c2bf619958f363e58d2e43363',
    'wqmnx1': 'MDEyNjM1M3B3ZC92ZGFuaHN2Jj0zLjIzNzBpNUw7cjZOIGlSKWxLMyBNaWUgbS44MmlhLzMyczRVLTUxT0NIKigp',
    '__wga': '1586651514515.1586649190828.1583414565242.1583414565242.10.2',
    'shshshsID': 'dcab6953f600e143916ad8ca71f3fdb0_11_1586651514929',
}

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36',
    'Sec-Fetch-Dest': 'script',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Referer': 'https://wqs.jd.com/pglive/index_main/index.html?sceneval=2&ptag=138631.36.18',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = (
    ('source', 'pglive'),
    ('dwAccountType', '22'),
    ('strPrePin', '200210'),
    ('_', '1586651516200'),
    ('sceneval', '2'),
    ('g_login_type', '1'),
    ('callback', 'jsonpCBKC'),
    ('g_ty', 'ls'),
)

response = requests.get('https://wq.jd.com/vaccount/GetAccountInfo', headers=headers, params=params, cookies=cookies)
print(response.text)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://wq.jd.com/vaccount/GetAccountInfo?source=pglive&dwAccountType=22&strPrePin=200210&_=1586651516200&sceneval=2&g_login_type=1&callback=jsonpCBKC&g_ty=ls', headers=headers, cookies=cookies)
