from threading import Thread
import tkinter as tk
from tkinter import ttk
from getaccno import getaccno
from getreverse import send_request
from startreverse import scan

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        import datetime

        # 获取当前日期
        current_date = datetime.date.today()

        # 输入cooKie
        self.cookie_label = tk.Label(self, text="1.请输入cookie：")
        self.cookie_label.pack(side="top", fill="x")

        self.cookie_entry = tk.Entry(self)
        self.cookie_entry.pack(side="top", fill="x")

        # 开始时间
        self.date_label = tk.Label(self, text="2.请选择开始日期和时间：")
        self.date_label.pack(side="top", fill="x")

        self.date_frame = tk.Frame(self)
        self.date_frame.pack(side="top")

        self.year_label = tk.Label(self.date_frame, text="年")
        self.year_label.pack(side="left")

        self.year_combobox = ttk.Combobox(self.date_frame, values=list(range(current_date.year, 2030)), width=5, state="readonly")
        self.year_combobox.pack(side="left")
        self.year_combobox.current(0)

        self.month_label = tk.Label(self.date_frame, text="月")
        self.month_label.pack(side="left")

        self.month_combobox = ttk.Combobox(self.date_frame, values=list(range(current_date.month, 13)), width=3, state="readonly")
        self.month_combobox.pack(side="left")
        self.month_combobox.current(0)

        self.day_label = tk.Label(self.date_frame, text="日")
        self.day_label.pack(side="left")

        self.day_combobox = ttk.Combobox(self.date_frame, values=list(range(current_date.day, 32)), width=3, state="readonly")
        self.day_combobox.pack(side="left")
        self.day_combobox.current(0)

        self.hour_label = tk.Label(self.date_frame, text="时")
        self.hour_label.pack(side="left")

        self.hour_combobox = ttk.Combobox(self.date_frame, values=list(range(24)), width=3, state="readonly")
        self.hour_combobox.pack(side="left")
        self.hour_combobox.current(0)

        self.minute_label = tk.Label(self.date_frame, text="分")
        self.minute_label.pack(side="left")

        self.minute_combobox = ttk.Combobox(self.date_frame, values=list(range(60)), width=3, state="readonly")
        self.minute_combobox.pack(side="left")
        self.minute_combobox.current(0)

        self.second_label = tk.Label(self.date_frame, text="秒")
        self.second_label.pack(side="left")

        self.second_combobox = ttk.Combobox(self.date_frame, values=list(range(60)), width=3, state="readonly")
        self.second_combobox.pack(side="left")
        self.second_combobox.current(0)

        # 结束时间
        self.enddate_label = tk.Label(self, text="3.请选择结束日期和时间：")
        self.enddate_label.pack(side="top", fill="x")

        self.enddate_frame = tk.Frame(self)
        self.enddate_frame.pack(side="top")

        self.end_year_label = tk.Label(self.enddate_frame, text="年")
        self.end_year_label.pack(side="left")

        self.end_year_combobox = ttk.Combobox(self.enddate_frame, values=list(range(current_date.year, 2030)), width=5, state="readonly")
        self.end_year_combobox.pack(side="left")
        self.end_year_combobox.current(0)

        self.end_month_label = tk.Label(self.enddate_frame, text="月")
        self.end_month_label.pack(side="left")

        self.end_month_combobox = ttk.Combobox(self.enddate_frame, values=list(range(current_date.month, 13)), width=3, state="readonly")
        self.end_month_combobox.pack(side="left")
        self.end_month_combobox.current(0)

        self.end_day_label = tk.Label(self.enddate_frame,text="日")
        self.end_day_label.pack(side="left")

        self.end_day_combobox = ttk.Combobox(self.enddate_frame, values=list(range(current_date.day, 32)), width=3, state="readonly")
        self.end_day_combobox.pack(side="left")
        self.end_day_combobox.current(0)

        self.end_hour_label = tk.Label(self.enddate_frame, text="时")
        self.end_hour_label.pack(side="left")

        self.end_hour_combobox = ttk.Combobox(self.enddate_frame, values=list(range(24)), width=3, state="readonly")
        self.end_hour_combobox.pack(side="left")
        self.end_hour_combobox.current(0)

        self.end_minute_label = tk.Label(self.enddate_frame, text="分")
        self.end_minute_label.pack(side="left")

        self.end_minute_combobox = ttk.Combobox(self.enddate_frame, values=list(range(60)), width=3, state="readonly")
        self.end_minute_combobox.pack(side="left")
        self.end_minute_combobox.current(0)

        self.end_second_label = tk.Label(self.enddate_frame, text="秒")
        self.end_second_label.pack(side="left")

        self.end_second_combobox = ttk.Combobox(self.enddate_frame, values=list(range(60)), width=3, state="readonly")
        self.end_second_combobox.pack(side="left")
        self.end_second_combobox.current(0)

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

    def get_selected_date(self, date_comboboxes):
        year = date_comboboxes[0].get()
        month = date_comboboxes[1].get()
        day = date_comboboxes[2].get()
        hour = date_comboboxes[3].get()
        minute = date_comboboxes[4].get()
        second = date_comboboxes[5].get()

        # 将日期和时间拼接成字符串
        selected_date = f"{year}-{month.zfill(2)}-{day.zfill(2)} {hour.zfill(2)}:{minute.zfill(2)}:{second.zfill(2)}"
        
        return selected_date

    def send_date(self):
        # 获取开始时间和结束时间
        selected_start_date = self.get_selected_date([
            self.year_combobox,
            self.month_combobox,
            self.day_combobox,
            self.hour_combobox,
            self.minute_combobox,
            self.second_combobox
        ])
        selected_end_date = self.get_selected_date([
            self.end_year_combobox,
            self.end_month_combobox,
            self.end_day_combobox,
            self.end_hour_combobox,
            self.end_minute_combobox,
            self.end_second_combobox
        ])

        res_json = send_request(selected_start_date.replace(" ", "").replace("-", "")[:8],self.cookie_entry.get())
        if(res_json["message"]=="用户未登录，请重新登录"):
            self.devname_listbox.insert("end", "用户未登录，请重新登录")

        devnames = [dev["devName"] for dev in res_json["data"]]
        devId = [dev["devId"] for dev in res_json["data"]]
        for i in range(len(devnames)):
            self.devname_listbox.insert("end", f"{devnames[i]} {devId[i]}")

    def start_resv(self):
        selected_indices = self.devname_listbox.curselection()
        selected_devnames = [self.devname_listbox.get(i) for i in selected_indices]
        selected_devId = [dev.split(" ")[1] for dev in selected_devnames]
        
        # 获取开始时间和结束时间
        selected_start_date = self.get_selected_date([
            self.year_combobox,
            self.month_combobox,
            self.day_combobox,
            self.hour_combobox,
            self.minute_combobox,
            self.second_combobox
        ])
        selected_end_date = self.get_selected_date([
            self.end_year_combobox,
            self.end_month_combobox,
            self.end_day_combobox,
            self.end_hour_combobox,
            self.end_minute_combobox,
            self.end_second_combobox
        ])
        stu_info=getaccno(selected_start_date.replace(" ", "")[:10],selected_end_date.replace(" ", "")[:10],self.cookie_entry.get())['data'][0]
        appAccNo = stu_info['appAccNo']
        syskind = 8
        t = Thread(target=scan, args=(syskind,appAccNo,selected_devId, selected_start_date, selected_end_date, self.cookie_entry.get(), self.result_listbox))
        t.start()

root = tk.Tk()
root.title(':-O')
app = App(master=root)
app.mainloop()
