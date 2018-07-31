#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 主界面函数MainPage.py

from tkinter import *
from view import *  #菜单栏对应的各个子页面


class MainPage(object):
    def __init__(self, master=None):
        self.root = master  #定义内部变量root
        self.root.geometry('%dx%d' % (600, 400))  #设置窗口大小
        self.initMenu()
        self.createPage()

    def createPage(self):
        self.inputPage = InputFrame(self.root)  # 创建不同Frame
        self.queryPage = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)
        self.inputPage.pack()  #默认显示数据录入界面

    def inputData(self):
        self.inputPage.pack()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def queryData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def countData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack()
        self.aboutPage.pack_forget()

    def aboutDisp(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack()

    def initMenu(self):
        menubar = Menu(self.root)
        menubar.add_command(label='数据录入', command=self.inputData)
        menubar.add_command(label='查询', command=self.queryData)
        menubar.add_command(label='统计', command=self.countData)
        menubar.add_command(label='关于', command=self.aboutDisp)
        self.root['menu'] = menubar  # 设置菜单栏
