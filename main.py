#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import tkinter as tk
from LoginPage import *
# import MainPage as MainPage

root = tk.Tk()

root.title('主程序')

# MainPage.MainPage(root)
LoginPage(root)

root.mainloop()
