#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter as gui
from common import set_window_center


class Init(gui.Toplevel):
    """关于窗口"""

    def __init__(self):
        gui.Toplevel.__init__(self)
        self.title("关于")
        set_window_center(self, 400, 400)
        self.resizable(False, False)
        self.init_page()

    def init_page(self):
        """加载控件"""
        gui.Label(self, text="关于界面").pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Label(self, text="你好你好你好你好")
        msg.pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Message(self, text="类似于弹出窗口，具有独立的窗口属性。", width=150)
        msg.pack()
        # gui.Label(self, text="你好你好你好你好").grid()
        # gui.Label(self, text="类似于弹出窗口，具有独立的窗口属性。", width=150).grid()
