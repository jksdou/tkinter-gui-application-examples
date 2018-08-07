#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 各类复用函数functions


def set_window_center(window, width, height):
    """设置窗口宽高及居中"""
    # 获取屏幕 宽、高
    w_s = window.winfo_screenwidth()
    h_s = window.winfo_screenheight()
    # 计算 x, y 位置
    x_co = (w_s - width) / 2
    y_co = (h_s - height) / 2 - 50
    window.geometry("%dx%d+%d+%d" % (width, height, x_co, y_co))
    window.minsize(width, height)


def get_screen_size(window):
    """获取屏幕 宽、高"""
    return window.winfo_screenwidth(), window.winfo_screenheight()


def get_window_size(window):
    """获取窗口 宽、高"""
    return window.winfo_reqwidth(), window.winfo_reqheight()


def treeview_sort_column(tv, col, reverse):
    """Treeview、列名、排列方式"""
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    # print(tv.get_children(''))
    l.sort(reverse=reverse)  # 排序方式
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):  # 根据排序后索引移动
        tv.move(k, '', index)
        # print(k)
    tv.heading(col, command=lambda: treeview_sort_column(
        tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
