#!/usr/bin/env python3
# -*- coding:utf-8-*-

import tkinter.messagebox
from tkinter import Button, Label, Tk

from lib.functions import set_window_center
from lib.sqlite_helper import DBHelper
from main import App


class InitWindow(Tk):
    """初始化窗口"""

    def __init__(self):
        Tk.__init__(self)
        self.title("初始化数据")
        set_window_center(self, 300, 180)
        self.resizable(False, False)
        self.win_success = None # 初始化成功的提示窗口
        self.init_page()

    def init_page(self):
        """加载控件"""
        btn_1 = Button(self, text="初始化数据库", command=self.do_init_db)
        btn_1.pack(expand="yes", padx=10, pady=10, ipadx=5, ipady=5)

    def do_init_db(self):
        """初始化"""
        db_helper = DBHelper()
        db_helper.reset_database()
        db_helper.create_database()
        try:
            tmp = db_helper.insert_user("admin", "admin")  # 默认用户
            tmp2 = db_helper.insert_content_by_username(
                "admin",
                "Hello World !",
                "源码仓库地址：https://github.com/doudoudzj/tkinter-app",
                "github",
            )
            tmp3 = db_helper.get_content_by_username("admin")
            print("添加用户admin:", tmp)
            print("添加内容:", tmp2)
            print("查询内容:", tmp3)
            self.do_success()
            self.destroy()
        except KeyError:
            print(KeyError)
            self.do_failed()

    def do_failed(self):
        """是否重试"""
        res = tkinter.messagebox.askretrycancel('提示', '初始化失败，是否重试？', parent=self)
        if res is True:
            self.do_init_db()
        elif res is False:
            self.destroy()

    def do_success(self):
        """初始化成功弹窗"""
        self.win_success = Tk()
        self.win_success.title("初始化成功")
        set_window_center(self.win_success, 250, 150)
        self.win_success.resizable(False, False)
        msg = Label(self.win_success, text="初始化成功")
        msg.pack(expand="yes", fill="both")

        btn = Button(self.win_success, text="确定", command=self.quit)
        btn.pack(side="right", padx=10, pady=10, ipadx=5, ipady=5)
        btn_open_app = Button(self.win_success, text="启动程序", command=self.open_app)
        btn_open_app.pack(side="right", padx=10, pady=10, ipadx=5, ipady=5)

    def open_app(self):
        """打开应用程序"""
        self.quit()
        self.win_success.destroy()
        self.win_success.quit()

        App()


if __name__ == "__main__":
    APP_INIT = InitWindow()
    APP_INIT.mainloop()
