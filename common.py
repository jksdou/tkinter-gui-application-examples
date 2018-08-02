#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


def set_window_center(window, w, h):
    """设置窗口宽高及居中"""
    # 获取屏幕 宽、高
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws - w) / 2
    y = (hs - h) / 2 - 50
    window.geometry("%dx%d+%d+%d" % (w, h, x, y))
    window.minsize(w, h)


def get_screen_size(window):
    return window.winfo_screenwidth(), window.winfo_screenheight()


def get_window_size(window):
    return window.winfo_reqwidth(), window.winfo_reqheight()
