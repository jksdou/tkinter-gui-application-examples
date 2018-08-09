#!/usr/bin/env python3
# -*- coding:utf-8-*-

import os
import sqlite3
import lib.global_variable as glv

class DBHelper(object):
    """sqlite helper"""

    def __init__(self):
        self.db_path = os.path.join(glv.get_variable("APP_PATH"), glv.get_variable("DATA_DIR"), 'database.db')
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()


    def create_database(self):
        """create table"""
        self.cursor.execute('''create table IF NOT EXISTS user(id INTEGER PRIMARY KEY, name TEXT, password TEXT)''')
        self.cursor.execute('''create table IF NOT EXISTS user_content(id INTEGER, userid INTEGER)''')
        self.cursor.execute('''create table IF NOT EXISTS content(id INTEGER, title TEXT, content TEXT, tag TEXT)''')
        self.cursor.execute('''create unique index IF NOT EXISTS user_unique_index on user(name)''')
        self.cursor.execute('''create unique index IF NOT EXISTS user_content_unique_index on user_content(id)''')
        self.cursor.execute('''create unique index IF NOT EXISTS content_unique_index on content(id)''')
        self.conn.commit()

    def reset_database(self):
        """drop table"""
        self.cursor.execute("DROP TABLE IF EXISTS user")
        self.cursor.execute("DROP TABLE IF EXISTS user_content")
        self.cursor.execute("DROP TABLE IF EXISTS content")
        self.conn.commit()
        self.create_database()

    def insert_user(self, name, password):
        """insert user"""
        name = name.strip()
        password = password.strip()
        info = name, password
        try:
            self.cursor.execute('INSERT INTO user(name, password) VALUES(?, ?)', info)
            self.conn.commit()
            return True
        except:
            return False

    def has_user(self, name, password):
        """check user"""
        name = name.strip()
        password = password.strip()
        info = name, password
        flag = self.cursor.execute(
            'SELECT * FROM user WHERE name=? and password=?',
            info).fetchall()
        if flag == []:
            return False
        else:
            return True

    def get_all_user_info(self):
        """get list of all user"""
        list = []
        rows = self.cursor.execute('SELECT id, name, password FROM user')
        for item in rows:
            list.append({
                'id': item[0],
                'name': item[1],
                'password': item[2]
            })
        return list

    def insert_content_by_username(self, username, title, content, tag):
        """insert content by username"""
        try:
            userid = self.cursor.execute('SELECT id FROM user WHERE name=?',
                (username, )).fetchone()
            count = self.cursor.execute('SELECT COUNT(*) FROM user_content').fetchone()
            rows = count[0]
            rows += 1
            self.cursor.execute(
                'INSERT INTO user_content(id, userid) VALUES (?, ?)',
                (rows, userid[0]))
            self.cursor.execute(
                'INSERT INTO content(id, title, content, tag) VALUES (?, ?, ?, ?)',
                (rows, title, content, tag))
            self.conn.commit()
            return True
        except:
            return False

    def get_content_by_username(self, name):
        """get content list of user by username"""
        list = []
        userid = self.cursor.execute(
            'SELECT id FROM user WHERE name=?', (name, )).fetchone()
        id = self.cursor.execute(
            'SELECT id FROM user_content WHERE userid=?', userid).fetchall()
        for item in id:
            if item is not None:
                r = self.cursor.execute(
                    'SELECT id, title, content, tag FROM content WHERE id=?',
                    item).fetchone()
                if r is not None:
                    list.append({
                        'id': r[0],
                        'title': r[1],
                        'content': r[2],
                        'tag': r[3]
                    })
        return list
