#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter as gui

from login import Login

root = gui.Tk()
root.resizable(False, False)

Login(root)

root.mainloop()
