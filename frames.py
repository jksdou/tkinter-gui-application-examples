#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter.messagebox
from tkinter import *
from tkinter import ttk

import dbcontent
from common import set_window_center, treeview_sort_column
from pages import winContentInfo, winContentEdit


class HomeFrame(Frame):  # 继承Frame类
    """应用主界面"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent  # 定义内部变量root
        self.init_page()

    def init_page(self):
        """加载控件"""
        lb1 = Label(self, text="用户:")
        lb1.grid(row=1, stick="W", pady=10)

        bt1 = Button(self, text="查看")
        bt1.grid(row=1, column=1, stick=E, pady=10)


class ContentAdd(Frame):
    """文章添加"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent  # 定义内部变量root
        self.content_title = StringVar()
        self.content = StringVar()
        self.content_tag = StringVar()
        self.init_page()

    def init_page(self):
        """加载控件"""
        Label(self).grid(row=0, stick=W, pady=10)

        lb1 = Label(self, text="标题: ")
        lb1.grid(row=1, stick=W, pady=10)

        et1 = Entry(self, textvariable=self.content_title)
        et1.grid(row=1, column=1, stick="we")

        lb2 = Label(self, text="内容: ")
        lb2.grid(row=2, stick="nw", pady=10)

        et2 = Text(self, height=10)
        sl = Scrollbar(et2)
        sl.config(command=et2.yview)
        # sl.grid(stick=N+S+E)
        sl.pack(side=RIGHT, fill=Y)
        et2.config(yscrollcommand=sl.set)
        # quote = """HAMLET: To b"""
        # et2.insert(END, quote)
        et2.grid(row=2, column=1, ipadx=10, stick="nswe")

        lb3 = Label(self, text="标签: ")
        lb3.grid(row=3, stick=W, pady=10)

        et3 = Entry(self, textvariable=self.content_tag)
        et3.grid(row=3, column=1, columnspan=2, stick="we")

        bt1 = Button(self, text="添加", command=self.do_add)
        bt1.grid(row=6, column=1, stick=E, pady=10)

    def do_add(self):
        """添加文章"""
        title = self.content_title.get()
        content = self.content.get()
        tag = self.content_tag.get()
        username = "admin"
        res = dbcontent.content_add(username, title, content, tag)
        if res is True:
            self.content_title.set("")
            self.content.set("")
            self.content_tag.set("")
            tkinter.messagebox.showinfo(title="成功", message="添加成功")
        else:
            tkinter.messagebox.showinfo(title="错误", message="添加失败")


class ContentList(Frame):
    """文章列表"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.list = []
        self.selected_item = None
        self.selected_name = tkinter.StringVar()
        self.win_content_info = None
        self.win_content_edit = None
        self.init_page()

    def init_page(self):
        """加载控件"""

        self.list = dbcontent.content_list()

        head_frame = tkinter.LabelFrame(self, text="文章操作")
        head_frame.grid(row=0, column=0, columnspan=2, sticky="nswe")
        tkinter.Label(head_frame, textvariable=self.selected_name).pack()

        btn_info = tkinter.Button(head_frame, text="详情", command=self.info)
        btn_info.pack(side="left")
        btn_edit = tkinter.Button(head_frame, text="编辑", command=self.edit)
        btn_edit.pack(side="left")
        btn_delete = tkinter.Button(head_frame, text="删除", command=self.delete)
        btn_delete.pack(side="left")

        # 表格
        self.tree_view = ttk.Treeview(self, show="headings")

        self.tree_view["columns"] = ("id", "title", "content", "tag")
        # 列设置
        self.tree_view.column("id", width=100)
        # self.tree_view.column("title", width=100)
        # self.tree_view.column("content", width=100)
        # self.tree_view.column("tag", width=100)
        # 显示表头
        self.tree_view.heading("id", text="ID")
        self.tree_view.heading("title", text="标题")
        self.tree_view.heading("content", text="内容")
        self.tree_view.heading("tag", text="标签")

        # 插入数据
        num = 1
        for item in self.list:
            self.tree_view.insert("", num, text="", values=(
                item["id"], item["title"], item["content"], item["tag"]))
        # 选中行
        self.tree_view.bind("<<TreeviewSelect>>", self.select)

        # 排序
        for col in self.tree_view["columns"]:  # 给所有标题加
            self.tree_view.heading(col, text=col, command=lambda _col=col: treeview_sort_column(
                self.tree_view, _col, False))

        vbar = ttk.Scrollbar(self, orient="vertical",
                             command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vbar.set)
        self.tree_view.grid(row=1, column=0, sticky="nsew")
        vbar.grid(row=1, column=1, sticky="ns")

    def select(self, event):
        """选中"""
        # event.widget获取Treeview对象，调用selection获取选择所有选中的
        slct = event.widget.selection()[0]
        self.selected_item = self.tree_view.item(slct)
        self.selected_name.set(self.selected_item["values"][1])
        # print("you clicked on ", self.selected_item)
        # print(self.selected_name)

    def info(self):
        """详情"""
        print("详情", self.selected_item)
        if self.selected_item is None:
            tkinter.messagebox.showinfo("提示", "请先选择")
        else:
            if self.win_content_info is not None and (
                hasattr(self.win_content_info.destroy, '__call__')):
            # if self.win_content_info and self.win_content_info.destroy:
                self.win_content_info.destroy()
            self.win_content_info = winContentInfo.Init(self.selected_item)
            # self.win_content_info = winAbout.Init()

    def edit(self):
        """编辑"""
        print("编辑", self.selected_item)
        if self.selected_item is None:
            tkinter.messagebox.showinfo("提示", "请先选择")
        else:
            if self.win_content_edit and self.win_content_edit.destroy:
                self.win_content_edit.destroy()
            self.win_content_edit = winContentEdit.Init(self.selected_item)

    def delete(self):
        """删除"""
        print(self.selected_item)
        tkinter.messagebox.showinfo("删除？", self.selected_item)  # 弹出消息提示框


class CountFrame(Frame):
    """文章统计"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.init_page()

    def init_page(self):
        """加载控件"""
        Label(self, text="统计界面").pack()


class AboutFrame(Frame):
    """关于界面"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.init_page()

    def init_page(self):
        """加载控件"""
        # Label(self, text="关于界面").grid()
        Label(self, text="你好你好你好你好").grid()
        Label(self, text="类似于弹出窗口，具有独立的窗口属性。", width=150).grid()


class UserListFrame(Frame):
    """用户列表界面"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.list = dbcontent.user_list()
        self.init_page()

    def init_page(self):
        """加载控件"""

        # Label(self, text="所有用户").grid(sticky="w")

        head_frame = tkinter.LabelFrame(self, text="用户操作")
        head_frame.grid(row=0, column=0, columnspan=2, sticky="nswe")
        left = tkinter.Label(head_frame, text="Inside the LabelFrame")
        left.pack()

        btn_info = tkinter.Button(head_frame, text="详情").pack(side="left")
        btn_edit = tkinter.Button(head_frame, text="编辑").pack(side="left")
        btn_reset = tkinter.Button(head_frame, text="重置密码").pack(side="left")
        btn_delete = tkinter.Button(head_frame, text="删除").pack(side="left")

        # 表格
        tree = ttk.Treeview(self, show="headings")

        tree["columns"] = ("id", "name", "password", "op")

        # tree.column("id", width=100) # 表示列,不显示
        # tree.column("name", width=100)
        # tree.column("password", width=100)
        # tree.column("op", width=100)
        # 显示表头
        tree.heading("id", text="ID")
        tree.heading("name", text="姓名")
        tree.heading("password", text="密码")
        tree.heading("op", text="操作")

        # 插入数据
        num = 1
        for item in self.list:
            tree.insert("", num, text="", values=(
                item["id"], item["name"], item["password"], "详情"))
        # tree.pack()
        vbar = ttk.Scrollbar(self, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vbar.set)
        tree.grid(row=1, column=0, sticky="nsew")
        vbar.grid(row=1, column=1, sticky="ns")
        Label(self, text="底部操作栏").grid(sticky="swe")

    def userArticle(self, event):
        print("用户文章", self)
        print("用户文章1", event)

    def userInfo(self, userid):
        print("用户详情", userid)

    def userEdit(self, userid):
        print("用户编辑", userid)

    def userDelete(self, userid):
        print("用户删除", userid)


class UserAddFrame(Frame):
    """用户添加"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.username = StringVar()
        self.password = StringVar()
        self.init_page()

    def init_page(self):
        """加载控件"""
        Label(self).grid(row=0, stick=W)

        Label(self, text="账户: ").grid(row=1, stick=W, pady=10)
        username = Entry(self, textvariable=self.username)
        username.grid(row=1, column=1, stick=E)

        Label(self, text="密码: ").grid(row=2, stick=W, pady=10)
        password = Entry(self, textvariable=self.password, show="*")
        password.grid(row=2, column=1, stick=E)

        button_login = Button(self, text="添加", command=self.do_add)
        button_login.grid(row=3, column=1, stick=W, pady=10)

    def do_add(self):
        """添加帐号"""
        # print(event)
        username = self.username.get()
        password = self.password.get()
        res = dbcontent.user_add(username, password)
        if res is True:
            self.username.set("")
            self.password.set("")
            tkinter.messagebox.showinfo(title="成功", message="添加成功")
        else:
            tkinter.messagebox.showinfo(title="错误", message="账号已存在")
