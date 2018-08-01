#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter as gui
import tkinter.messagebox

from common import set_window_center
from menu import initLoginMenu
from page import MainPage


class Login(object):
    def __init__(self, master=None):
        if self.isLoggedIn() is True:
            MainPage(master)
        else:
            self.root = master
            self.root.title("账号登陆")
            # self.root.geometry("%dx%d" % (300, 180))  # 设置窗口大小
            set_window_center(self.root, 300, 180)
            # 定义变量
            self.username = gui.StringVar()
            self.password = gui.StringVar()
            self.initPage()

    def initPage(self):
        self.page = gui.Frame(self.root)  # 创建Frame
        self.page.pack()
        initLoginMenu(self.root)
        gui.Label(self.page).grid(row=0, stick=gui.W)
        gui.Label(self.page, text="账户: ").grid(row=1, stick=gui.W, pady=10)
        gui.Entry(self.page, textvariable=self.username).grid(
            row=1, column=1, stick=gui.E
        )
        gui.Label(self.page, text="密码: ").grid(row=2, stick=gui.W, pady=10)
        gui.Entry(self.page, textvariable=self.password, show="*").grid(
            row=2, column=1, stick=gui.E
        )
        gui.Button(self.page, text="登陆", command=self.doLogin).grid(
            row=3, column=1, stick=gui.W, pady=10
        )
        gui.Button(self.page, text="退出", command=self.page.quit).grid(
            row=3, column=1, stick=gui.E
        )

    def doLogin(self):
        n = self.username.get()
        p = self.password.get()
        if n == "admin" and p == "admin":
            self.page.destroy()
            MainPage(self.root)
        else:
            tkinter.messagebox.showinfo(title="错误", message="账号或密码错误！")

    def isLoggedIn(self):
        # return True
        return False
