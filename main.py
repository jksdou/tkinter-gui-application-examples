#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
from tkinter import Tk

import lib.global_variable as glv
from pages import frameLogin


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        # 全局变量
        glv._init()
        glv.set("APP_PATH", os.path.dirname(__file__)) # 当前目录
        glv.set("DATA_DIR", "data")

        frameLogin.Login(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
