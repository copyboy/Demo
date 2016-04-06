# -*- coding:utf-8 -*-

__author__ = 'Yuriy'
'''
6–4. 算术. 更新上一章里面你的得分测试练习方案,把测试得分放到一个列表中去.你的代
码应该可以计算出一个平均分,见练习 2-9 和练习 5-3.
'''


li = [12,43,12,6,280]
i = 0
values = 0
for i in range(len(li)):
	values += li[i]
print values / float(len(li))