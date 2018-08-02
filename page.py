#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter as gui
import frames

from menu import initMenu
from common import set_window_center


class MainPage(object):
    def __init__(self, master=None):
        self.page = master
        set_window_center(self.page, 800, 600)
        initMenu(self)
        self.initFrame()
        self.initDefaultPage()

    def initFrame(self):
        """创建不同的Frame"""
        self.pageHome = frames.HomeFrame(self.page)
        self.pageAdd = frames.InputFrame(self.page)
        self.pageQuery = frames.QueryFrame(self.page)
        self.pageCount = frames.CountFrame(self.page)
        self.pageContact = frames.AboutFrame(self.page)
        self.pageUserList = frames.UserListFrame(self.page)
        self.pageUserAdd = frames.UserAddFrame(self.page)

    def initDefaultPage(self):
        """加载默认界面"""
        self.currentPage = self.pageHome
        self.page.title("应用主界面")
        self.currentPage.pack()

    def openPage(self, pageName, pageTitle):
        """打开界面的通用函数"""
        self.page.title(pageTitle)
        if hasattr(self, "currentPage"):
            self.currentPage.pack_forget()
        if hasattr(self, pageName):
            self.currentPage = getattr(self, pageName)
            self.currentPage.pack()
        else:
            print("错误")

    def openHome(self):
        self.openPage("pageHome", "应用主界面")

    def inputData(self):
        self.openPage("pageAdd", "文章添加")

    def queryData(self):
        self.openPage("pageQuery", "文章查询")

    def countData(self):
        self.openPage("pageCount", "文章统计")

    def openContact(self):
        self.openPage("pageContact", "联系我们")

    def openUser(self):
        page = gui.Toplevel()
        page.title("用户详情")
        page.resizable(False, False)
        set_window_center(page, 200, 150)

        # gui.Label(page).grid(row=0, stick=gui.W, pady=2)

        gui.Label(page, text="姓名: ").grid(row=1, stick=gui.W, pady=2)
        gui.Label(page, text="管理员").grid(row=1, column=1, stick=gui.E)

        gui.Label(page, text="账户: ").grid(row=2, stick=gui.W, pady=2)
        gui.Label(page, text="admin").grid(row=2, column=1, stick=gui.E)

        gui.Label(page, text="密码: ").grid(row=3, stick=gui.W, pady=2)
        gui.Label(page, text="admin").grid(row=3, column=1, stick=gui.E)


    def openUserList(self):
        self.openPage("pageUserList", "用户列表")

    def openUserAdd(self):
        self.openPage("pageUserAdd", "用户添加")

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
