from concurrent.futures import ThreadPoolExecutor ,as_completed
import threading
import requests
from loguru import logger
exit_thread = threading.Event()
from tkinter import messagebox

cookies = {
    'ic-cookie': '',
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


def start_xourse(syskind,appAccNo,resvdev,resvBeginTime,resvEndTime,self):
    json_data = {
    'sysKind': syskind,#系统类型
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
        logger.info(res_json['message'])
        if(res_json['message']=="新增成功"):
           messagebox.showinfo("Success", "预定“"+resvdev+"”成功")
           exit_thread.set()
           return
        self.insert("end", res_json['message'])
        
def scan(syskind,appAccNo,resvdevs,resvBeginTime,resvEndTime,cookie,self):
    cookies['ic-cookie']=cookie 
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(start_xourse, syskind, appAccNo, i, resvBeginTime, resvEndTime, self): i for i in resvdevs}
        for future in as_completed(futures):
            if exit_thread.is_set():
                executor.shutdown(wait=False)
                break
            try:
                self.insert("end", future.result())
            except Exception as e:
                logger.error(e)       
            