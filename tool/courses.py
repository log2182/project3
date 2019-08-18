#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 17:07
# @Author  : zx-long  
# @File    : courses.py
class Courses:
    def __init__(self,school_id,name,period,price,score = None,teacher = None):
        self.name = name
        self.period = period
        self.price = price
        self.score = score
        self.school_id = school_id
        self.students = []
        self.teacher = teacher
