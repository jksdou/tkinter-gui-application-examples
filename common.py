#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


def set_window_center(window, w, h):
    """设置窗口宽高及居中"""
    # 获取屏幕 宽、高
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry("%dx%d+%d+%d" % (w, h, x, y))
