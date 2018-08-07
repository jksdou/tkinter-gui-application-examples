#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter as gui
import tkinter.messagebox

import lib.dbcontent as dbcontent
from lib.functions import set_window_center
from menu import initLoginMenu
from view import MainPage


class Login(object):
    def __init__(self, master=None):
        if self.isLoggedIn() is True:
            MainPage(master)
        else:
            self.root = master
            self.root.title("账号登陆")
            set_window_center(self.root, 300, 180)
            # 定义变量
            self.username = gui.StringVar()
            self.password = gui.StringVar()
            self.initPage()

    def initPage(self):
        initLoginMenu(self.root)
        self.page = gui.Frame(self.root)  # 创建Frame
        self.page.pack()

        gui.Label(self.page).grid(row=0, stick="W")

        gui.Label(self.page, text="账户: ").grid(row=1, stick="W", pady=10)
        username = gui.Entry(self.page, textvariable=self.username)
        username.grid(row=1, column=1, stick="E")
        username.bind("<Return>", self.returnEnvent)

        gui.Label(self.page, text="密码: ").grid(row=2, stick="W", pady=10)
        password = gui.Entry(self.page, textvariable=self.password, show="*")
        password.grid(row=2, column=1, stick="E")
        password.bind("<Return>", self.returnEnvent)

        button_login = gui.Button(self.page, text="登陆", command=self.doLogin)
        button_login.grid(row=3, column=1, stick="W", pady=10)

        button_cancel = gui.Button(self.page, text="退出", command=self.doCancel)
        button_cancel.grid(row=3, column=1, stick="E")

    def doLogin(self):
        username = self.username.get()
        password = self.password.get()
        res = dbcontent.user_login(username, password)
        if res is True:
            # if username == "admin" and password == "admin": # 测试账号
            self.page.destroy()
            MainPage(self.root)
        else:
            tkinter.messagebox.showinfo(title="错误", message="账号或密码错误！")

    def doCancel(self):
        self.page.quit()

    def returnEnvent(self, event):
        self.doLogin()

    def isLoggedIn(self):
        # return True
        return False
