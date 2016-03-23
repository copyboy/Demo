# coding:utf-8
__author__ = 'Yuriy'

'''
5-17 随机数。熟读随机数模块然后解下面的题：
生成一个有 N 个元素的由随机数 n 组成的列表， 其中 N 和 n 的取值范围分别为： (1 <
N <= 100), (0 <= n <= 231 -1)。然后再随机从这个列表中取 N (1 <= N <= 100)个随机数
出来， 对它们排序，然后显示这个子集。
题目解读：N个元素的列表，元素来源于range(231)
		应该是从该列表中随机选择M个元素排序 1 <= M <= N
'''

import random

N = random.randint(1, 100)
li = []
for i in range(N):
	li.append(random.randint(0, 230))

print li
print N
print len(li)

ul = []
M = random.randint(1, N)
for i in range(M):
	ul.append(random.choice(li))


print ul
print M
print len(ul)

print sorted(ul)