#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""程序入口文件"""

import os
from tkinter import Tk

import lib.global_variable as glv
from pages import frameLogin, win_splah


# Load global variable management module
glv.init_global_variable()
glv.set_variable("APP_PATH", os.path.dirname(__file__))  # 当前目录
glv.set_variable("DATA_DIR", "data")


class App(Tk):
    """Application Class"""

    def __init__(self):
        Tk.__init__(self)

        # Login Window
        frameLogin.Login(self)

        self.mainloop()


if __name__ == "__main__":
    win_splah.Splah()
    App()
