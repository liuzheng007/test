# -*- coding: utf-8 -*-
#
#2017-09-14
#writen by liuzheng
#two function is_leap_year 判断是否闰年 day_in_month 每月天数
tu_days_in_month=0,31,28,31,30,31,30,31,31,30,31,30,31
def is_leap_year(y):
    if y%4==0 and y%100 or y%400==0:
	    return True
    else:   #冒号
	    return False #大小写问题


def days_in_month(y,m):     
    if is_leap_year(y) and m==2:  #冒号用英文的
	    return 29
    else:                       #注意缩进逻辑
	    return tu_days_in_month[m] #数组用方括号
	