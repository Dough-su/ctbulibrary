import requests
import re
import time
from threading import Thread
cookies = {
    'ic-cookie': 'c07f63df-6606-4f98-9d87-b6436d1b232f',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'DNT': '1',
    'Origin': 'https://ic.ctbu.edu.cn',
    'Referer': 'https://ic.ctbu.edu.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'lan': '1',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


def start_xourse(appAccNo,resvdev,resvBeginTime,resvEndTime,self):
    json_data = {
    'sysKind': 8,#系统类型
    'appAccNo': appAccNo,#学号
    'memberKind': 1,#成员类型
    'resvMember': [#学号
        appAccNo
    ],
    'resvBeginTime': ''+resvBeginTime+'',
    'resvEndTime': ''+resvEndTime+'',
    'testName': '',
    'captcha': '',
    'resvProperty': 0,
    'resvDev': [
        resvdev,
    ],
    'memo': '',
}
    while True:
        response = requests.post('https://ic.ctbu.edu.cn/ic-web/reserve', cookies=cookies, headers=headers, json=json_data)
        res_json = response.json()
        print(str(res_json["message"]))
        self.insert("end", res_json['message'])
        
def scan(appAccNo,resvdevs,resvBeginTime,resvEndTime,cookie,self):
    cookies['ic-cookie']=cookie 
    while True:
        for i in resvdevs:
            #启动线程
            t = Thread(target=start_xourse,args=(appAccNo,i,resvBeginTime,resvEndTime,self))
            t.start()            
            
   