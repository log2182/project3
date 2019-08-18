#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 19:57
# @Author  : zx-long  
# @File    : school.py


class School:
    def __init__(self, name, id):
        self.name = name
        self.courses = []
        self.id = id

    def del_course(self):
        self.check_courses()
        while True:
            num = input('输入要删除的课程编号:').strip()
            if num.isdigit() and 1 <= int(num) <= len(self.courses):
                del self.courses[int(num)-1]
                return True,'删除成功'
            else:
                return False,'课程编号不存在'

    def check_courses(self):
        print(('已开设课程-%s'% self.name).center(50,'='))
        for k, course in enumerate(self.courses, 1):
            print(k, course.name, course.period, '￥'+str(course.price))
