#!/usr/bin/env python3
# -*- coding:utf-8-*-

from SQLiteHelper import DBHelper

if __name__ == '__main__':
    db = DBHelper()
    db.create_database()
    tmp = db.insert_user('admin', 'admin') # 默认用户
    tmp2 = db.insert_content_by_username('admin','测试内容标题', '源码仓库地址：https://github.com/doudoudzj/tkinter-app', 'github')
    tmp3 = db.get_content_by_username('admin')
    print(tmp, tmp2, tmp3)
