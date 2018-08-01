#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter as gui
import frames

from menu import initMenu
from common import set_window_center


class MainPage(object):
    def __init__(self, master=None):
        self.page = master
        set_window_center(self.page, 600, 400)
        initMenu(self)
        self.initPage()
        self.openPage("pageQuery", "查询")  # 默认打开界面

    def initPage(self):
        self.pageAdd = frames.InputFrame(self.page)  # 创建不同Frame
        self.pageQuery = frames.QueryFrame(self.page)
        self.pageCount = frames.CountFrame(self.page)
        self.pageContact = frames.AboutFrame(self.page)

    def openPage(self, pageName, pageTitle):
        self.page.title(pageTitle)
        if hasattr(self, "currentPage"):
            self.currentPage.pack_forget()
        if hasattr(self, pageName):
            self.currentPage = getattr(self, pageName)
            self.currentPage.pack()
        else:
            print("错误")

    def inputData(self):
        self.openPage("pageAdd", "添加")

    def queryData(self):
        self.openPage("pageQuery", "查询")

    def countData(self):
        self.openPage("pageCount", "统计")

    def openContact(self):
        self.openPage("pageContact", "联系我们")

    def openDownload(self):
        x = gui.Toplevel()
        x.title("下载管理")
        set_window_center(x, 400, 400)
        msg = gui.Label(x, text="你好你好你好你好")
        msg.pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Message(x, text="类似于弹出窗口，具有独立的窗口属性。", width=150)
        msg.pack()

    def openUpload(self):
        x = gui.Toplevel()
        x.title("上传管理")
        set_window_center(x, 400, 400)
        msg = gui.Label(x, text="你好你好你好你好")
        msg.pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Message(x, text="类似于弹出窗口，具有独立的窗口属性。", width=150)
        msg.pack()

    def openSynchronize(self):
        x = gui.Toplevel()
        x.title("同步管理")
        set_window_center(x, 400, 400)
        msg = gui.Label(x, text="你好你好你好你好")
        msg.pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Message(x, text="类似于弹出窗口，具有独立的窗口属性。", width=150)
        msg.pack()

    def openBackup(self):
        x = gui.Toplevel()
        x.title("备份管理")
        set_window_center(x, 400, 400)
        msg = gui.Label(x, text="你好你好你好你好")
        msg.pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Message(x, text="类似于弹出窗口，具有独立的窗口属性。", width=150)
        msg.pack()
