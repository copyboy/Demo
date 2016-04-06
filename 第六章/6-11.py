# -*- coding:utf-8 -*-
__author__ = 'Yuriy'

'''
6–11.转换
(a)创建一个从整数到 IP 地址的转换程序,如下格式: WWW.XXX.YYY.ZZZ.
	解：输入1个整数，把这个整数换成32位的2进制，八位一组，每组就是一部分的地址
(b)更新你的程序,使之可以逆转换.
	解：IP地址到整数，字符串用点号分割为4个元素的列表，每个元素转换为8位二进制，再拼接这4个8位，然后int(s,base=2) 转换为整数
		嫌这题比较烦，不想写了、、、先这样吧。
	'''

def intTo32(ch):
	li = ''
	if ch < 0 or ch > pow(2, 32) - 1:
		print 'Error ,Please input correct number(0~2^32-1)'
		return
	else:

		li = bin(ch).replace('0b', '')
# 		print type(li)
	length = len(li)
	# print length
	if length < 32:
		li = '0' * ( 32 - length ) + li

	# print len(li)
	return li

# print intTo32(12345)


def int2IP(ch):

	li = intTo32(ch)
	# print li
	i = j = 0
	ul = []
	sx = []
	if li:
		while i < 32:
			ul.append(li[i:i+8])        # 把整个字符串分成4个部分的列表
			i += 8
		while j < 4:
			sx.append(int(ul[j], base=2))     # int() 函数可以指定进制
			j += 1
		return '.'.join([str(x) for x in sx])  # join 函数给字符串列表中间添加点号
	else:
		return

def main():
	print 'input a number (0~2^32-1)'
	while True:
		ch = raw_input('>>>')
		try:
			ch = int(ch)
		except Exception:
			print 'Input Number!'
			continue
		else:
			print int2IP(ch)
			continue

if __name__ == '__main__':
	main()
	# 最大值为 4294967295


# ch2 = lambda x: '.'.join([str(x/(256**i)%256) for i in range(3,-1,-1)])
#  这里是别人写的一段转换的代码，比较牛X，写的时候完全想不起来这样写
