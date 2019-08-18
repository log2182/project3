#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 14:59
# @Author  : zx-long  
# @File    : student.py
from db import db_handler
from conf import settings
from lib import common

stu_logger = common.get_logger('stu')

class Student:
    def __init__(self, name, stu_id, psd, school_id=None):
        self.name = name
        self.id = stu_id
        self.psd = psd
        self.school_id = school_id
        self.courses = []

    def show_score(self):
        print('=========成绩=========')
        for k,item in enumerate(self.courses,1):
            print(k,item.name,item.score)

    def add_course(self, name):
        sch = db_handler.select(settings.sch_DB, self.school_id)
        for item in self.courses:
            if item.name == name:
                return False, '这门课程已在学习课程内'
        for item in sch.courses:
            if item.name == name:
                item.students.append(self)
                self.courses.append(item)
                db_handler.save(settings.stu_DB, self)
                db_handler.save(settings.sch_DB, sch)
                stu_logger.info('学生姓名%s，id:%s,增加了课程%s' % (self.name, self.id, name))
                return True, '课程已加入清单'
        else:
            return False, '课程不存在'

    def choose_school(self,school_id):
        if db_handler.select(settings.sch_DB, school_id):
            self.school_id = school_id
            return True, '成功选择学校'
        else:
            return False, '不存在的学校ID'

    # 查看所在学校的开课情况
    def show_courses_inschool(self):
       sch = db_handler.select(settings.sch_DB,self.school_id)
       sch.check_courses()
