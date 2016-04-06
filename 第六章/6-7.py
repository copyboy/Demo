# -*- coding:utf-8 -*-
__author__ = 'Yuriy'

'''
6–7. 调试.看一下在例 6.5 中给出的代码(buggy.py)
(a)研究这段代码并描述这段代码想做什么.在所有的(#)处都要填写你的注释.
(b)这个程序有一个很大的问题,比如输入 6,12,20,30,等它会死掉,实际上它不能处理任何的偶
数,找出原因.
(c)修正(b)中提出的问题.
'''


num_str = raw_input('Enter a number: ')

# raw_input 输入的是字符串，转化为整数
num_num = int(num_str)

# 把输入的整数转化为从1开始，长度为输入整数的列表
fac_list = range(1, num_num+1)
print "BEFORE:", fac_list      # 原文错误，加了引号不能输出fac_list 结果

# 置i为0
i = 0
li = []
# 遍历该列表
while i < len(fac_list):

	# 删去能被输入整数整除的列表值
	# if num_num % fac_list[i] == 0:
	# 	# print fac_list[i]
	# 	# print fac_list
	# 	del fac_list[i]  # 错误在这里，当你删除一个列表元素后，该列表也变化了
	# 这样改：当不为0时，添加到另一个新建的列表中

	if num_num % fac_list[i] != 0:
		li.append(fac_list[i])
	# i自增
	i = i + 1


# 输出处理过的列表
print "AFTER:", li
