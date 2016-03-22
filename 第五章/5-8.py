# coding:utf-8
__author__ = 'Yuriy'

'''
5-8 几何。计算面积和体积：
(a) 正方形 和 立方体
(b) 圆 和 球
'''

def recArea():
	x = float(raw_input('正方形的边长：'))
	y = x**2
	print '正方形的面积为 %.2f' % y
	return y

def recSize():
	x = float(raw_input('立方体的边长：'))
	y = x**3
	print '立方体的体积为 %.2f' % y
	return y

def cyArea():
	r = float(raw_input('圆的半径：'))
	y = 3.14*r*r
	print '圆的面积为 %.2f' % y
	return y

def cySize():
	r = float(raw_input('圆的半径：'))
	y = 4*3.14*pow(r, 3)/3
	print '圆的体积为 %.2f' % y
	return y
def default():
	default = 'input error ,input again!'
	print default


def show():
	while True:
		str = '''
func 1.正方形
func 2.立方体
func 3.圆
func 4.球
	'''
		print str
		ch = raw_input("input func number:")

		# msg = {'1': recArea(), '2': recSize(), '3': cyArea(), '4': cySize()} #在这里就直接调用了value上的函数
		# msg.get(ch, default)
		msg = {'1': 'recArea()', '2': 'recSize()', '3': 'cyArea()', '4': 'cySize()'}
		try:
			eval(msg.get(ch))  #调用eval函数执行字符串格式的函数名
		except Exception:
			default()
if __name__ == '__main__':
	show()