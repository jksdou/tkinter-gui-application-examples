#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
from tkinter import Tk

import lib.global_variable as glv
from pages import frameLogin


class App(Tk):
    """Application Class"""

    def __init__(self):
        Tk.__init__(self)

        # Load global variable management module
        glv._init()
        glv._set("APP_PATH", os.path.dirname(__file__)) # 当前目录
        glv._set("DATA_DIR", "data")

        # Login Window
        frameLogin.Login(self)


if __name__ == "__main__":
    APP_INIT = App()
    APP_INIT.mainloop()
