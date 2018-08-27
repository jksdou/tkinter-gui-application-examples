#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.sqlite_helper import DBHelper


def user_login(username, password):
    """验证用户名及密码"""
    if username is None or password is None:
        return False
    else:
        # session['username'] = name
        _db = DBHelper()
        if _db.has_user(username, password):
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
        _db = DBHelper()
        return _db.insert_user(username, password)


def user_list():
    """用户列表"""
    _db = DBHelper()
    return _db.get_all_user_info()


def content_add(username, title, content, tag):
    """添加内容"""
    if username is None:
        return "账号不能为空"
    if content is None:
        return "内容不能为空"
    _db = DBHelper()
    return _db.insert_content_by_username(username, title, content, tag) is True

def content_list_by_username(username):
    """用户的所有文章"""
    if username is None:
        return "账号不能为空"

    _db = DBHelper()
    return _db.get_content_by_username(username)
