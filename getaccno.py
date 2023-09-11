import requests

cookies = {
    'ic-cookie': '',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Referer': 'https://ic.ctbu.edu.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'lan': '1',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'token': '',
    'x-forwarded-for': '1.1.1.1',
}

params = {
    'page': '1',
    'pageSize': '10',
    'resvBeginTime': '',
    'resvEndTime': '',
    'resvStatus': '262',
}
def getaccno(startdate,enddate,cookie):
    cookies['ic-cookie']=cookie
    params['resvBeginTime']=startdate
    params['resvEndTime']=enddate
    response = requests.get('https://ic.ctbu.edu.cn/ic-web/psgSeat/resvInfo', params=params, cookies=cookies, headers=headers)
    response_json=response.json()
    return response_json['data'][0]['appAccNo']