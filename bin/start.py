#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 23:37
# @Author  : zx-long  
# @File    : start.py

import sys, os

path = os.path.dirname(os.path.dirname(__file__))       # 这条命令用来获取当前文件所在文件夹的路径，这里是E-mall的路径
sys.path.append(path)                                # 把工程路径加入到环境变量中
from core import src
if __name__ == '__main__':
    src.run()

"""
学校类有一个课程对象列表，列表里存储着课程对象，课程对象里面存储着学生的信息
每个学生又保存着自己的课程对象，每个对象有自己的课程分数属性，
一门课对应一个老师，一个老师对应一个学校，一个老师可以对应多门课,老师的课程列表存储他授课的课程名称而不是对象，且保存一个学校ID
教师可以通过学校和自己存储的课程列表找到自己教的学生
分为：用户输入层——接口层（类）——数据处理层
bin：start启动程序
conf:settings 包括日志设置和存储路径设置
db:分四个数据包，各自储存学生，教师，管理员，学校的pickle文件，还有db_handler模块用于数据的提取与存储等
lib：包含common ,日志生成器
log:日志文件
tool:各种类
"""
