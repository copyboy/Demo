# coding:utf-8
__author__ = 'Yuriy'

'''
5-12 系统限制。写一段脚本确认一下你的 Python 所能处理的整数，长整数，浮点数和复
数的范围。
大体思路是一个整数左移，直到溢出。
但是在写的时候，while循环那里不能正确输出结果.
查资料结果就是导入sys模块。。。
'''
import sys
print sys.maxint
a = sys.maxint
print bin(a)
print len(str(bin(a).replace('0b', ''))) #查看整型的长度


print sys.float_info
print sys.maxint
print -sys.maxint-1
print sys.float_info.max
print sys.float_info.min

# a = 1
# i = 0
# while True:
# 	try:
# 		print '数字：%d' % a
# 		a = a << 1
# 		print '数字：%d' % a
#
# 		i += 1
# 	except:
# 		print i
# 		break
