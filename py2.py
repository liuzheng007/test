# -*- coding: utf-8 -*-
#
#2017-09-14
#writen by liuzheng
#two function is_leap_year �ж��Ƿ����� day_in_month ÿ������
tu_days_in_month=0,31,28,31,30,31,30,31,31,30,31,30,31
def is_leap_year(y):
    if y%4==0 and y%100 or y%400==0:
	    return True
    else:   #ð��
	    return False #��Сд����


def days_in_month(y,m):     
    if is_leap_year(y) and m==2:  #ð����Ӣ�ĵ�
	    return 29
    else:                       #ע�������߼�
	    return tu_days_in_month[m] #�����÷�����
	