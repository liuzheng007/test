# -*- coding: utf-8 -*-
#
#2017-09-15
#writen by liuzheng
#
from can_2_3_tool import *
i_year=0      #pathon ÿ�������治��Ҫ�ֺ�
i_month=0

i_year=input("���������  pls input year==>")
i_month=input("�������·� pls import month==>")



out_str="  SUN    MON    TUE    WEN    THU    FRI     SAT "

i=0
wd=0
print_days=days_in_month(i_year,i_month)
for i in range(print_days+wd):
    pd=i+1-wd	 #0��31����
	 
    if i%7==0:
        bl_str='\n{:^7d}'.format(pd)  #�·��ټ�������,i��бƲ
    else:                           # ������ð�� 
	    bl_str='{:^7d}'.format(pd)		#�ո���˫���Ű�����
    out_str=out_str+bl_str
	 
print out_str