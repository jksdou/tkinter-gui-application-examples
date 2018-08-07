#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Content Edit

import tkinter as gui
from lib.functions import set_window_center


class Init(gui.Toplevel):
    """内容编辑窗口"""

    def __init__(self, info=None):
        gui.Toplevel.__init__(self)
        self.current_content = info
        self.win_title = "内容编辑《" + self.current_content["values"][1] + "》"
        self.title(self.win_title)
        set_window_center(self, 400, 500)
        self.resizable(False, False)
        self.init_page()

    def init_page(self):
        """加载控件"""
        gui.Label(self, text="title").pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Label(self, text="你好你好你好你好")
        msg.pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Message(self, text=self.current_content, width=150)
        msg.pack()
        # gui.Label(self, text="你好你好你好你好").grid()
        # gui.Label(self, text="类似于弹出窗口，具有独立的窗口属性。", width=150).grid()
