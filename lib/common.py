#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 22:54
# @Author  : zx-long  
# @File    : common.py

import logging.config
from conf import settings


def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)   # dictConfig是用字典配置日志的格式，另外还有fileConfig，basicConfig
    logger = logging.getLogger(name)
    return logger
