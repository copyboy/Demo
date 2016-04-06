# -*- coding:utf-8 -*-
__author__ = 'Yuriy'

'''
6–17.方法.实现一个叫 myPop()的函数,功能类似于列表的 pop()方法,用一个列表作为输入,
移除列表的最新一个元素,并返回它.
'''

def myPop(li):
	if len(li) != 0:
		tmp = li[-1]
		del li[-1]
		return tmp
	else:
		return

li = [2]
print myPop(li)
print li