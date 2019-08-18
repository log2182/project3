#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 15:14
# @Author  : zx-long  
# @File    : db_handler.py
import os
from conf import settings
import pickle

# 保存用户信息
def save(path,obj):
    user_path = os.path.join(path, '%s.pickle' % obj.id)
    with open(user_path, 'wb') as f:
        pickle.dump(obj, f)
        f.flush()

# 取出用户信息
def select(path,id):
    user_path = os.path.join(path, '%s.pickle' % id)
    if os.path.exists(user_path):                                  # 判断文件是否存在
        with open(user_path, 'rb') as f:
            obj = pickle.load(f)
            return obj
    else:
        return None

# 遍历文件夹,寻找学校id和名称
def show_sch_info():
    for i in os.walk(settings.sch_DB):
        for n in range(len(i[2])):
            path = os.path.join(i[0],i[2][n])
            with open(path,'rb') as f:
                obj = pickle.load(f)
                print(obj.name,obj.id)
