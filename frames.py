#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter.messagebox import *

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
        self.initPage()

    def initPage(self):
        Label(self, text="用户列表页面内容").pack()
        Label(self, text="你好你好你好你好").pack(expand=YES, fill=BOTH)
        Label(self, text="类似于弹出窗口，具有独立的窗口属性。", width=150).pack()


class UserAddFrame(Frame):
    """用户添加"""

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.initPage()

    def initPage(self):
        Label(self, text="用户添加页面内容").pack()
        Label(self, text="你好你好你好你好").pack(expand=YES, fill=BOTH)
        Label(self, text="类似于弹出窗口，具有独立的窗口属性。", width=150).pack()
