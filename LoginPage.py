#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 登陆界面函数LoginPage.py

from tkinter import *
import tkinter.messagebox as message
import MainPage as MainPage


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry("%dx%d" % (300, 180))  # 设置窗口大小
        self.root.title("账号登陆")
        self.username = StringVar()
        self.password = StringVar()
        self.initPage()

    def initPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text="账户: ").grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text="密码: ").grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show="*").grid(
            row=2, column=1, stick=E
        )
        Button(self.page, text="登陆", command=self.loginCheck).grid(
            row=3, stick=W, pady=10
        )
        Button(self.page, text="退出", command=self.page.quit).grid(
            row=3, column=1, stick=E
        )

    def loginCheck(self):
        n = self.username.get()
        p = self.password.get()
        if n == "admin" and p == "admin":
            self.page.destroy()
            MainPage.MainPage(self.root)
        else:
            message.showinfo(title="错误", message="账号或密码错误！")
