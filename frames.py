#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter.messagebox
from tkinter import *
from tkinter import ttk

import dbcontent
from common import set_window_center


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
        et1.grid(row=1, column=1, stick=W+E)

        lb2 = Label(self, text="内容: ")
        lb2.grid(row=2, stick=N+W, pady=10)

        et2 = Text(self, height=10)
        sl = Scrollbar(et2)
        sl.config(command=et2.yview)
        # sl.grid(stick=N+S+E)
        sl.pack(side=RIGHT, fill=Y)
        et2.config(yscrollcommand=sl.set)
        # quote = """HAMLET: To b"""
        # et2.insert(END, quote)
        et2.grid(row=2, column=1, ipadx=10, stick=W+N+S+E)

        lb3 = Label(self, text="标签: ")
        lb3.grid(row=3, stick=W, pady=10)

        et3 = Entry(self, textvariable=self.content_tag)
        et3.grid(row=3, column=1, columnspan=2, stick=W+E)

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
        self.root = parent  # 定义内部变量root
        self.list = []
        self.init_page()

    def init_page(self):
        """加载控件"""
        self.list = dbcontent.content_list()
        lb1 = Label(self, text="ID", width=10, fg="black", bg="#ddd")
        lb1.grid(row=0, column=0, sticky="WE")

        lb2 = Label(self, text="标题", width=20, fg="black", bg="#ddd")
        lb2.grid(row=0, column=1, sticky="WE")

        lb3 = Label(self, text="内容", width=20, fg="black", bg="#ddd")
        lb3.grid(row=0, column=2, sticky="WE")

        lb4 = Label(self, text="标签", width=20, fg="black", bg="#ddd")
        lb4.grid(row=0, column=3, columnspan=5, sticky="WE")

        # print(self.list)
        num = 1
        for item in self.list:
            lb1 = Label(self, text=item["id"], relief=RIDGE)
            lb1.grid(row=num, column=0, sticky="WE")
            lb2 = Label(self, text=item["title"], relief=RIDGE)
            lb2.grid(row=num, column=1, sticky="WE")
            lb3 = Label(self, text=item["content"], relief=RIDGE)
            lb3.grid(row=num, column=2, sticky="WE")
            lb4 = Label(self, text=item["tag"], relief=RIDGE)
            lb4.grid(row=num, column=3, sticky="WE")

            bt1 = Button(self, text="文章")
            bt1.grid(row=num, column=4, sticky="WE")
            bt2 = Button(self, text="详情")
            bt2.grid(row=num, column=5, sticky="WE")
            bt3 = Button(self, text="编辑")
            bt3.grid(row=num, column=6, sticky="WE")
            bt4 = Button(self, text="删除")
            bt4.grid(row=num, column=7, sticky="WE")
            num = num + 1


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
        self.user_list = dbcontent.user_list()
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
        r = 1
        for item in self.user_list:
            tree.insert("", r, text="" , values=(item["id"], item["name"], item["password"], "详情"))
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
