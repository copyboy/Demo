__author__ = 'Yuriy'
# -*- coding : utf-8 -*-

while True:
	try:
		str1 = raw_input()
	except:
		break
	num = (len(str1) - 1) / 8
	num_2 = 8 - len(str1) % 8
	str1 += '0' * num_2

	for i in range(num + 1):
		print str1[i * 8:i * 8 + 8]