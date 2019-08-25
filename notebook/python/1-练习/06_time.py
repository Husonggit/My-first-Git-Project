#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "HS"

import time

t = time.time()

#输出本地时间 
# 格式：time.struct_time(tm_year=2019, tm_mon=4, tm_mday=8, tm_hour=13, tm_min=23, tm_sec=43, tm_wday=0, tm_yday=98, tm_isdst=0)

print(time.localtime())
print(time.localtime(t))

#生成struc_time 
