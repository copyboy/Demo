__author__ = 'Yuriy'

li = [12,43,12,6,280]
i = 0
values = 0
for i in range(len(li)):
	values += li[i]
print values / float(len(li))