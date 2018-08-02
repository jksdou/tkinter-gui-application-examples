#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import *
import tkinter.messagebox

import dbcontent
from common import set_window_center


class HomeFrame(Frame):  # 继承Frame类
    """应用主界面"""

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.initPage()

    def initPage(self):
        Label(self, text="用户:").grid(row=1, stick=W, pady=10)
        Button(self, text="查看").grid(row=6, column=1, stick=E, pady=10)


class InputFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.itemName = StringVar()
        self.importPrice = StringVar()
        self.sellPrice = StringVar()
        self.deductPrice = StringVar()
        self.initPage()

    def initPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text="药品名称: ").grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.itemName).grid(row=1, column=1, stick=E)
        Label(self, text="进价 /元: ").grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.importPrice).grid(row=2, column=1, stick=E)
        Label(self, text="售价 /元: ").grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.sellPrice).grid(row=3, column=1, stick=E)
        Label(self, text="优惠 /元: ").grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.deductPrice).grid(row=4, column=1, stick=E)
        Button(self, text="录入").grid(row=6, column=1, stick=E, pady=10)


class QueryFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.itemName = StringVar()
        self.initPage()

    def initPage(self):
        Label(self, text="查询界面").pack()


class CountFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.initPage()

    def initPage(self):
        Label(self, text="统计界面").pack()


class AboutFrame(Frame):
    """关于界面"""

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.initPage()

    def initPage(self):
        # Label(self, text="关于界面").pack()
        Label(self, text="你好你好你好你好").pack(expand=YES, fill=BOTH)
        Label(self, text="类似于弹出窗口，具有独立的窗口属性。", width=150).pack()


class UserListFrame(Frame):
    """用户列表界面"""

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.list = []

    def initPage(self):

        self.list = dbcontent.user_list()
        # print(self.list)
        Label(self, text="ID", width=10, fg="black", bg="#ddd").grid(row=0, column=0, sticky=W + E)
        Label(self, text="姓名", width=20, fg="black", bg="#ddd").grid(row=0, column=1, sticky=W + E)
        Label(self, text="密码", width=20, fg="black", bg="#ddd").grid(row=0, column=2, sticky=W + E)
        Label(self, text="操作", width=20, fg="black", bg="#ddd").grid(row=0, column=3, columnspan=4, sticky=W + E)

        r = 1
        for item in self.list:
            Label(self, text=item["id"], relief=RIDGE).grid(row=r, column=0, sticky=W + E)
            Label(self, text=item["name"], relief=RIDGE).grid(row=r, column=1, sticky=W + E)
            Label(self, text=item["password"], relief=RIDGE).grid(row=r, column=2, sticky=W + E)
            Button(self, text="文章", command=lambda: self.userArticle(item)).grid(row=r, column=3, sticky=W + E)
            Button(self, text="详情", command=lambda: self.userInfo(item)).grid(row=r, column=4, sticky=W + E)
            Button(self, text="编辑", command=lambda: self.userEdit(item)).grid(row=r, column=5, sticky=W + E)
            Button(self, text="删除", command=lambda: self.userDelete(item)).grid(row=r, column=6, sticky=W + E)
            r = r + 1

        # count = 0
        # l = len(self.list)
        # while count < l:
        #     cur = count
        #     Label(self, text=self.list[count]["id"], relief=RIDGE).grid(row=count, column=0, sticky=W + E)
        #     Label(self, text=self.list[count]["name"], relief=RIDGE).grid(row=count, column=1, sticky=W + E)
        #     Label(self, text=self.list[count]["password"], relief=RIDGE).grid(row=count, column=2, sticky=W + E)
        #     Button(self, text="文章", command=lambda: self.userArticle(self.list[cur])).grid(row=count, column=3, sticky=W + E)
        #     Button(self, text="详情", command=lambda: self.userInfo(self.list[cur])).grid(row=count, column=4, sticky=W + E)
        #     Button(self, text="编辑", command=lambda: self.userEdit(self.list[cur])).grid(row=count, column=5, sticky=W + E)
        #     Button(self, text="删除", command=lambda: self.userDelete(self.list[cur])).grid(row=count, column=6, sticky=W + E)
        #     count = count + 1
        # else:
        #     print (count, "结束")


        Label(self, text="底部操作栏").grid(sticky=W + E + S)

    def userArticle(self, userid):
        print("用户文章", userid)

    def userInfo(self, userid):
        print("用户详情", userid)

    def userEdit(self, userid):
        print("用户编辑", userid)

    def userDelete(self, userid):
        print("用户删除", userid)

class UserAddFrame(Frame):
    """用户添加"""

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.username = StringVar()
        self.password = StringVar()
        self.initPage()

    def initPage(self):
        Label(self).grid(row=0, stick=W)

        Label(self, text="账户: ").grid(row=1, stick=W, pady=10)
        username = Entry(self, textvariable=self.username)
        username.grid(row=1, column=1, stick=E)

        Label(self, text="密码: ").grid(row=2, stick=W, pady=10)
        password = Entry(self, textvariable=self.password, show="*")
        password.grid(row=2, column=1, stick=E)

        button_login = Button(self, text="添加", command=self.doAdd)
        button_login.grid(row=3, column=1, stick=W, pady=10)

    def doAdd(self):
        # print(event)
        n = self.username.get()
        p = self.password.get()
        res = dbcontent.user_add(n, p)
        if res is True:
            self.username.set("")
            self.password.set("")
            tkinter.messagebox.showinfo(title="成功", message="账号" + n + "添加成功")
        else:
            tkinter.messagebox.showinfo(title="错误", message="账号已存在")
