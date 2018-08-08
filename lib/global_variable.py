#!/usr/bin/env python3
# -*- coding:utf-8-*-
# global variable management module


def _init():
    """initialize variable"""
    global GLOBALS_DICT
    GLOBALS_DICT = {}


def _set(name, value):
    """set variable"""
    try:
        GLOBALS_DICT[name] = value
        return True
    except KeyError:
        return False


def _get(name):
    """get variable"""
    try:
        return GLOBALS_DICT[name]
    except KeyError:
        return "Not Found"
