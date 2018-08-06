#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter as gui

import frames
from common import set_window_center
from menu import InitMenu
from pages import winAbout

class MainPage():
    """主界面"""
    def __init__(self, master=None):
        self.page = master
        set_window_center(self.page, 800, 600)
        InitMenu(self)
        self.current_frame = None
        # 初始化Frames
        self.page_frame = {
            "home": frames.HomeFrame,
            "content_add": frames.ContentAdd,
            "content_list": frames.ContentList,
            "count": frames.CountFrame,
            "contact": frames.AboutFrame,
            "user_list": frames.UserListFrame,
            "user_add": frames.UserAddFrame
        }
        self.open_home()
        self.win_about = None

    def open_page(self, frame_name, title):
        """打开/更换主界面的通用函数"""
        self.page.title(title)
        # 先销毁之前frame
        if self.current_frame is not None and (hasattr(self.current_frame.destroy, '__call__')):
            self.current_frame.destroy()

        self.current_frame = self.page_frame[frame_name](self.page)
        self.current_frame.pack()
        # for (key, val) in self.page_frame.items():
        #     self.page_frame[key].destroy()
        # self.page.title(title)
        # self.page_frame[frame_name].pack()

    def open_home(self):
        """应用主界面"""
        self.open_page("home", "应用主界面")

    def open_content_add(self):
        """文章添加"""
        self.open_page("content_add", "文章添加")

    def open_content_list(self):
        """文章列表"""
        self.open_page("content_list", "文章查询")

    def open_content_count(self):
        """文章统计"""
        self.open_page("count", "文章统计")

    def open_ontact(self):
        """联系我们"""
        self.open_page("contact", "联系我们")

    def open_user_info(self):
        """用户详情"""
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

    def open_user_list(self):
        """用户列表"""
        self.open_page("user_list", "用户列表")
        # self.page_frame['user_list'].init_data()

    def open_user_add(self):
        """用户添加"""
        self.open_page("user_add", "用户添加")

    def openDownload(self):
        """下载窗口"""
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

    def open_about(self):
        """关于窗口"""
        if self.win_about and self.win_about.destroy:
            self.win_about.destroy()
        self.win_about = winAbout.Init()
