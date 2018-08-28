#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import Toplevel, Label, Message
from components import frames, menu
from lib.functions import set_window_center
from pages import winAbout


class MainPage():
    """主界面"""

    def __init__(self, master=None):
        self.root = master # 主窗口
        set_window_center(self.root, 800, 600)
        menu.MainMenu(self) # 使用self可以传递主窗口和主窗口操作函数
        # 初始化Frames
        self.current_frame = None
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
        self.root.title(title)
        # 先销毁之前frame
        if self.current_frame is not None and (hasattr(self.current_frame.destroy, '__call__')):
            self.current_frame.destroy()

        self.current_frame = self.page_frame[frame_name](self.root)
        self.current_frame.pack()

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
        page = Toplevel()
        page.title("用户详情")
        page.resizable(False, False)
        set_window_center(page, 200, 150)

        # Label(page).grid(row=0, stick="w", pady=2)

        Label(page, text="姓名: ").grid(row=1, stick="w", pady=2)
        Label(page, text="管理员").grid(row=1, column=1, stick="e")

        Label(page, text="账户: ").grid(row=2, stick="w", pady=2)
        Label(page, text="admin").grid(row=2, column=1, stick="e")

        Label(page, text="密码: ").grid(row=3, stick="w", pady=2)
        Label(page, text="admin").grid(row=3, column=1, stick="e")

    def open_user_list(self):
        """用户列表"""
        self.open_page("user_list", "用户列表")
        # self.page_frame['user_list'].init_data()

    def open_user_add(self):
        """用户添加"""
        self.open_page("user_add", "用户添加")

    def open_download(self):
        """下载窗口"""
        root = Toplevel()
        root.title("下载管理")
        set_window_center(root, 400, 400)
        msg = Label(root, text="你好你好你好你好")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="类似于弹出窗口，具有独立的窗口属性。", width=150)
        msg.pack()

    def open_upload(self):
        """上传管理"""
        root = Toplevel()
        root.title("上传管理")
        set_window_center(root, 400, 400)
        msg = Label(root, text="你好你好你好你好")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="类似于弹出窗口，具有独立的窗口属性。", width=150)
        msg.pack()

    def open_synchronize(self):
        """同步管理"""
        root = Toplevel()
        root.title("同步管理")
        set_window_center(root, 400, 400)
        msg = Label(root, text="你好你好你好你好")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="类似于弹出窗口，具有独立的窗口属性。", width=150)
        msg.pack()

    def open_backup(self):
        """备份管理"""
        root = Toplevel()
        root.title("备份管理")
        set_window_center(root, 400, 400)
        msg = Label(root, text="你好你好你好你好")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="类似于弹出窗口，具有独立的窗口属性。", width=150)
        msg.pack()

    def open_about(self):
        """关于窗口"""
        if self.win_about and self.win_about.destroy:
            self.win_about.destroy()
        self.win_about = winAbout.Init()

    def window_to_top(self):
        """窗口置顶"""
        self.root.attributes('-topmost', True)

    def window_not_top(self):
        """窗口置顶"""
        self.root.attributes('-topmost', False)
