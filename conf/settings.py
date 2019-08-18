#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 15:15
# @Author  : zx-long  
# @File    : settings.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))   # StudentManageSys文件夹路径
BASE_DB = os.path.join(BASE_DIR, 'db')              # db文件夹路径
mng_DB = os.path.join(BASE_DB,'mng')
sch_DB = os.path.join(BASE_DB,'sch')
stu_DB = os.path.join(BASE_DB,'stu')
teac_DB = os.path.join(BASE_DB,'teac')
BASE_LOG =os.path.join(BASE_DIR,'log')              # log文件夹路径

standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'               # 其中name为getLogger指定的名字

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式 结束

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(BASE_LOG):            # isdir判断文件夹是否存在
    os.mkdir(BASE_LOG)

# log文件的全路径
logfile_path = os.path.join(BASE_LOG, 'log.log')

# log配置字典
LOGGING_DIC = {
    'version': 1,

    'disable_existing_loggers': False,         # 决定已存在的日志器是否有效

    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },

    'filters': {},

    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',  # 打印到屏幕，此为必选项，是打印方式的选择
            'formatter': 'simple'
        },
        # 打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },

    'loggers': {
        # 该字典对象每个元素的key为要定义的日志器名称，value为日志器的配置信息组成的dcit,信息包括level、handlers、filters 等
        # 将成为logging.getLogger(__name__)拿到的logger配置,
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'INFO',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },

}
