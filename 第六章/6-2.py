# -*- coding:utf-8 -*-
__author__ = 'Yuriy'

'''
6–2. 字符串标识符.修改例 6-1 的 idcheck.py 脚本,使之可以检测长度为一的标识符,并且
可以识别 Python 关键字,对后一个要求,你可以使用 keyword 模块(特别是 keyword.kwlist)来帮你.
'''

import string,keyword

alphas = string.letters + '_'
nums = string.digits
keywd = keyword.kwlist                      #更改1

print 'Welcome to the Identifier Checker v2.0'  #更改1
print 'Testees must be at least 1 chars long.'
myInput = raw_input('Identifier to test? ')

if len(myInput) >= 1:             #更改3
	if myInput[0] not in alphas:
		print '''invalid: first symbol must be
			alphabetic'''
	else:
		for otherChar in myInput[1:]:
			if otherChar not in alphas + nums:
				print '''invalid: remaining
					symbols must be alphanumeric'''
				break
		else:
			if myInput in keywd:        #更改4
				print 'identifier is  keyword'
			else:
				print 'okay as an identifier'
