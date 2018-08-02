#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from SQLiteHelper import DBHelper


def user_login(username, password):
    """验证用户名及密码"""
    if username is None or password is None:
        return False
    else:
        # session['username'] = name
        db = DBHelper()
        if db.has_user(username, password):
            return True
        else:
            return False


def user_add(username, password):
    """账号添加"""
    if username is None:
        return "账号不能为空"
    if password is None:
        return "密码不能为空"
    if (username is not None) and (password is not None):
        db = DBHelper()
        return db.insert_user(username, password)


def user_list():
    """用户列表"""
    db = DBHelper()
    return db.get_all_user_info()

