import requests

cookies = {
    'ic-cookie': 'cacf6e9e-f325-423b-8839-f8d21c3c3117',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'ic-cookie=24d2723c-8c11-4476-9501-0efc086e9757',
    'DNT': '1',
    'Referer': 'https://ic.ctbu.edu.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'lan': '1',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'token': '2a9aa5eefb0f476abb0265bb9941ac8f',
}

params = {
    'roomIds': '100455854',
    'resvDates': '20230404',
    'sysKind': '8',
}
def send_request(datetime,cookie):
 print('开始获取')
 cookies['ic-cookie']=cookie
 params['resvDates']=datetime
 response = requests.get('https://ic.ctbu.edu.cn/ic-web/reserve', params=params, cookies=cookies, headers=headers)
 return response.json()