#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import tkinter as gui

import lib.global_variable as glv
from login import Login

glv._init()

glv.set("APP_PATH", os.path.dirname(__file__))
glv.set("DATA_DIR", "data")

ROOT = gui.Tk()

Login(ROOT)

ROOT.mainloop()
