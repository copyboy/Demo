# -*- coding:utf-8 -*-
__author__ = 'Yuriy'

'''
6–9. 转换.为练习 5-13 写一个姊妹函数, 接受分钟数, 返回小时数和分钟数. 总时间不
变,并且要求小时数尽可能大.
'''

def min2hour(min):
	if min > 60 * 24 or min < 0:
		print 'Input Error ,Try again'
	li = divmod(min, 60)
	print '现在是%d时，%d分' % li

if __name__ == '__main__':
	while True:
		try:
			ch = int(raw_input('输入分钟数：'))
		except Exception:
			print '输入错误，请重新输入'
			continue
		min2hour(ch)