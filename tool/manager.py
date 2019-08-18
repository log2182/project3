#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 14:59
# @Author  : zx-long  
# @File    : manager.py
from tool import school, teacher, courses
from db import db_handler
from conf import settings
from lib import common

mng_logger = common.get_logger('mng')

class Manager:
    def __init__(self,name,id,psd):
        self.name = name
        self.id = id
        self.psd = psd

    def create_school(self,name, school_id):
        sch = db_handler.select(settings.sch_DB, school_id)
        if sch:
            return False, 'id已被其他学校占用'
        else:
            sch_obj = school.School(name, school_id)
            db_handler.save(settings.sch_DB, sch_obj)
            mng_logger.info('管理员-id:%s 创建了学校，学校id:%s,名称:%s' % (self.id, school_id, name))
            return True, '学校创建成功'


    def create_teacher(self,school_id, name, id, psd, ):
        sch = db_handler.select(settings.sch_DB, school_id)
        tch = db_handler.select(settings.teac_DB, id)
        if sch:
            if not tch:
                tch_obj = teacher.Teacher(name, id, psd, school_id)
                db_handler.save(settings.teac_DB, tch_obj)
                mng_logger.info('管理员id:%s 创建了老师，老师id:%s,名称:%s' % (self.id, id, name))
                return True, '创建成功'
            else:
                return False, 'id 已被占用'
        else:
            return False, '不存在的学校id'

    def create_course(self,school_id, name, period, price):
        sch = db_handler.select(settings.sch_DB, school_id)
        cors = courses.Courses(school_id, name, period, price)
        sch.courses.append(cors)
        db_handler.save(settings.sch_DB, sch)
        mng_logger.info('管理员-id:%s 在学校-%s增加了课程-%s' % (self.id, sch.name, name))
        return True, '成功创建课程'

    @classmethod    # 可以直接用类调用方法而且不用实例化
    def show_school(self):
        print('========已建立的学校========')
        db_handler.show_sch_info()


    def del_course(self,school_id):
        sch = db_handler.select(settings.sch_DB, school_id)
        if sch:
            if sch.del_course():
                db_handler.save(settings.sch_DB, sch)
                return True,'成功删除'
            else:
                return False,'编号错误'
        else:
            return False,'学校id错误'
