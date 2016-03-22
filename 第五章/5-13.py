# coding:utf-8
__author__ = 'Yuriy'

'''
5-13 转换。写一个函数把由小时和分钟表示的时间转换为只用分钟表示的时间。
'''
def htom(h, m):
	res = h*60 + m
	return res

def show():
	while True:
		ch = raw_input('\ninput time. like 15:24\n>>>')
		li = ch.split(':')
		# print li
		if len(li) != 2:                       # 验证是不是严格按照冒号分开的时间格式
			print 'input error,please again!'
			continue
		try:                                    # 验证输入的格式是数字，而不是字母
			a = int(li[0])
			b = int(li[1])
		except Exception:
			print 'input error,please again!'
			continue
		if 0 < a < 25 and 0 < b < 61:          # 判断小时跟分钟的是否越界
			print htom(a, b)
		else:
			print 'incorrect time type ,input again!'
if __name__ == '__main__':
	show()