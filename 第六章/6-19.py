# -*- coding:utf-8 -*-
__author__ = 'Yuriy'

'''
6–19.多列输出.有任意项的序列或者其他容器,把它们等距离分列显示.由调用者提供数据和
输出格式.例如,如果你传入 100 个项并定义 3 列输出,按照需要的模式显示这些数据.这种情况下,应
该是两列显示 33 个项,最后一列显示 34 个.你可以让用户来选择水平排序或者垂直排序.
水平排序：第一行33，第二行33，第三行34
垂直排序：第一行3，第二行3.。。。第33行3，第34行1个
'''

# def fmatPrint(ch, li):
# print '''input display type:
# 1:Horizontal Sorting
# 	2:Vertical Sorting
# 	'''
# 	choice = raw_input('>>>')

import random

list = []
nums = input("pls input a number for iterms: ")
clns = input("pls input a number for columns: ")
for i in range(0, nums):
	list.append(i + 1)
print list
print '0 horizontal sort'
print '1 vertical sort'
print '2 quit'
while True:
	print
	i = input("pls input operation number: ")
	if (2 == i):
		break
	elif (i < 0 or i > 2):
		print 'Error input operation, try agin. 3 operation is quit\n'
		continue
	if (0 == i):
		n = 0
		for m in range(0, nums):
			print "%4d" % list[m],
			n += 1
			if n % clns == 0:
				print
	elif (1 == i):
		n = 0
		for i in range(0, nums / clns + 1):
			if i == nums / clns:
				for j in range(0, nums % clns):
					print 4 * clns * ' ' + str(list[i * clns + j])
			else:
				for j in range(0, clns):
					print "%4s" % str(list[i + j * (nums / clns)]),
				print
			n += 1
			if n % clns == 0:
				continue