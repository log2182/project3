#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 20:38
# @Author  : zx-long  
# @File    : user.py
from db import db_handler
from tool import student, manager
from conf import settings
from lib import common

user_logger = common.get_logger('user')

class User:
    @classmethod
    def login_interface(self, option, id, password):
        path_dic = {'1': settings.stu_DB, '2':settings.teac_DB,'3': settings.mng_DB}
        path = path_dic[option]
        obj = db_handler.select(path,id)
        if obj:
            if obj.psd == password:
                user_logger.info('id: %s 登陆了' % (id))
                return obj, '登陆成功'
            else:
                return False,'密码错误'
        else:
            return False, 'id不存在'

    @classmethod
    def register_interface(self, option, name, id, password):
        dic = {'1': student.Student, '2': manager.Manager}
        path_dic = {'1':settings.stu_DB,'2':settings.mng_DB}
        path = path_dic[option]
        user_info = db_handler.select(path,id)        # 先从数据库查找是否有同名用户
        if user_info:
            return False, '账号已存在'         # return可以返回多个值
        else:
            obj = dic[option](name, id, password)
            db_handler.save(path,obj)
            user_logger.info('%s-id:%s 注册了' % (name,id))
            return True, '注册成功'
