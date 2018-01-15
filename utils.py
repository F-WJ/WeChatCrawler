# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = 2018 / 1 / 13
import html


def str_to_dict1(headers):
    # 字符串转字典
    headers = headers.split("\n")
    d_headers = dict()
    for h in headers:
        h = h.strip()
        if h:
            k, v = h.split(":", 1)
            d_headers[k] = v.strip()
    return d_headers


def sub_dict(d, keys):
    # 过滤无用字段
    return {k: html.unescape(d[k]) for k in d if k in keys}


def str_to_dict(s, join_symbol="\n", split_symbol=":"):
    s_list = s.split(join_symbol)
    data = dict()
    for item in s_list:
        item = item.strip()
        if item:
            k, v =item.split(split_symbol, 1)
            data[k] = v.strip()
    return data




