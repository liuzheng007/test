# -*- coding: utf-8 -*-
#
#2017-09-15
#writen by liuzheng
#
from can_2_3_tool import *
i_year=0      #pathon 每条语句后面不需要分号
i_month=0

i_year=input("请输入年份  pls input year==>")
i_month=input("请输入月份 pls import month==>")



out_str="  SUN    MON    TUE    WEN    THU    FRI     SAT "

i=0
wd=0
print_days=days_in_month(i_year,i_month)
for i in range(print_days+wd):
    pd=i+1-wd	 #0到31遍历
	 
    if i%7==0:
        bl_str='\n{:^7d}'.format(pd)  #月份再加上日子,i用斜撇
    else:                           # 后面有冒号 
	    bl_str='{:^7d}'.format(pd)		#空格用双引号包起来
    out_str=out_str+bl_str
	 
print out_str