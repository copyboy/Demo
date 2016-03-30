# coding:utf-8
__author__ = 'Yuriy'

import time

user = 'zlzg'
start = time.clock()

for i in range(1000):
	print 'it is a test input',user

usetime = time.clock() - start


started = time.clock()

for i in range(1000):
	print 'it is a test input %s' % user

usedtime = time.clock() - started

print usetime
print usedtime