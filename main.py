
from threading import Thread
import tkinter as tk

from getreverse import send_request
from startreverse import scan

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
            #输入cooKie
        self.cookie_label = tk.Label(self, text="1.请输入cookie：")
        self.cookie_label.pack(side="top", fill="x")

        self.cookie_entry = tk.Entry(self)
        self.cookie_entry.pack(side="top", fill="x")

        self.date_label = tk.Label(self, text="2.请输入开始日期 格式为yyyy-mm-dd hh:mm:ss：")
        self.date_label.pack(side="top", fill="x")

        self.date_entry = tk.Entry(self)
        self.date_entry.pack(side="top", fill="x")

        #结束时间
        self.enddate_label = tk.Label(self, text="3.请输入结束日期 格式为yyyy-mm-dd hh:mm:ss：")
        self.enddate_label.pack(side="top", fill="x")

        self.enddate_entry = tk.Entry(self)
        self.enddate_entry.pack(side="top", fill="x")

        


        self.ok_button = tk.Button(self, text="4.获取位置", command=self.send_date)
        self.ok_button.pack(side="left")

        self.devname_label = tk.Label(self, text="可选位置(按住ctrl点选即可连选)：")
        self.devname_label.pack()

        self.devname_listbox = tk.Listbox(self, selectmode="extended")
        self.devname_listbox.pack()

        self.start_button = tk.Button(self, text="5.开始预约", command=self.start_resv)
        self.start_button.pack()
        self.result_label = tk.Label(self, text="预约结果：")
        self.result_label.pack()

        self.result_listbox = tk.Listbox(self, selectmode="extended")
        self.result_listbox.pack()
        self.text_label = tk.Label(self, text="可接python(人工智能不接，接爬虫)，nodejs，springboot，等等项目。价格500起，如需要请联系oonqp7452@163.com")
        self.text_label.pack(side="bottom", fill="x")



    def send_date(self):
        date = self.date_entry.get()
        #转换为yyyymmdd
        date = date.replace("-", "")
        date = date.replace(" ", "")
        date = date.replace(":", "")
        date = date[:8]

        res_json = send_request(date,self.cookie_entry.get())
        if(res_json["message"]=="用户未登录，请重新登录"):
            self.devname_listbox.insert("end", "用户未登录，请重新登录")
        devnames = [dev["devName"] for dev in res_json["data"]]
        devId = [dev["devId"] for dev in res_json["data"]]
        print(devnames)
        for i in range(len(devnames)):
            self.devname_listbox.insert("end", devnames[i]+" "+str(devId[i]))
                

    def start_resv(self):
        selected_indices = self.devname_listbox.curselection()
        selected_devnames = [self.devname_listbox.get(i) for i in selected_indices]
        selected_devId = [dev.split(" ")[1] for dev in selected_devnames]
        t = Thread(target=scan, args=(selected_devId,self.date_entry.get(),self.enddate_entry.get(),self.cookie_entry.get(),self.result_listbox))
        t.start()

root = tk.Tk()
root.title('冰美式不加糖，重庆工商已被nepu占领,能给抖音的小小乐迪点个关注吗！她真的好可爱:-O')
app = App(master=root)
app.mainloop()
