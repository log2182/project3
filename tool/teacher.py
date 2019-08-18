#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 14:59
# @Author  : zx-long  
# @File    : teacher.py
from db import db_handler
from conf import settings
from lib import common
from core import src

teac_logger = common.get_logger('teac')

class Teacher:
    def __init__(self,name,id,psd,school_id):
        self.name = name
        self.id = id
        self.psd = psd
        self.school_id = school_id
        self.courses = []

    def show_courses(self):
        print('========查看您的授课========')
        for k,item in enumerate(self.courses,1):
            print(k,item)

    # 教师选课
    def add_course(self,option):
        sch = db_handler.select(settings.sch_DB, self.school_id)
        for item in self.courses:
            if option == item:
                return False, '课程已存在'
        else:
            for cour in sch.courses:
                if option == cour.name:
                    self.courses.append(option)  # 课程名称放入老师的课程列表
                    cour.teacher = self            # 将该门课程的教师属性设置为当前教师对象
                    db_handler.save(settings.sch_DB, sch)
                    db_handler.save(settings.teac_DB, self)
                    teac_logger.info('教师：姓名-%s，id-%s,增加了课程%s' % (self.name, self.id, option))
                    return True, '成功选择课程'
            else:
                return False, '没有目标课程'

    # 查看所授课班级相应的学生名单
    def show_students(self):
        sch = db_handler.select(settings.sch_DB, self.school_id)  # 取出学校
        for course in sch.courses:
            if course.name in self.courses:
                print('\n\n')
                print('=========%s=========' % course.name)
                for k, stu in enumerate(course.students, 1):
                    print(k, stu.name, 'id:' + stu.id)


    def set_score(self, course, id, score):
        stu = db_handler.select(settings.stu_DB, id)  # 取出学生对象，学生的课程列表里存放着课程对象，将对象的分数属性设置为想要的值
        if stu:
            for item in stu.courses:
                if item.name == course:
                    item.score = score
                    db_handler.save(settings.stu_DB, stu)
                    teac_logger.info(
                        '教师：姓名-%s，id-%s,修改了id为:%s学生的%s课的分数' % (src.user_obj.name, src.user_obj.id, id, course))
                    return True, '设置成功'
            else:
                return False, '课程不存在'
        else:
            return False, '学生ID错误'

    # 查看所在学校的开课情况
    def show_courses_inschool(self):
        sch = db_handler.select(settings.sch_DB, self.school_id)
        sch.check_courses()
