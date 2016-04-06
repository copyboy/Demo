# -*- coding:utf-8 -*-
__author__ = 'Yuriy'

'''
6–13.字符串.string 模块包含三个函数,atoi(),atol(),和 atof(),它们分别负责把字符串转
换成整数,长整型,和浮点型数字.从 Python1.5 起,Python 的内建函数 int(),long(),float()也可以
做相同的事了, complex()函数可以把字符串转换成复数.(然而 1,5 之前,这些转换函数只能工作于
数字之上)
string 模块中并没有实现一个 atoc()函数,那么你来实现一个,atoc(),接受单个字符串做参
数输入,一个表示复数的字符串,例如,'-1.23e+4-5.67j',返回相应的复数对象.你不能用 eval()函
数,但可以使用 complex()函数,而且你只能在如下的限制之下使用 complex():complex(real,imag)
的 real 和 imag 都必须是浮点值.
	解：考虑只有实数、只有虚数的情况。难点，分割字符串，使它成为实数、虚数部分。
'''


def atoc(_str):
	'''
	这段代码是从网上copy下来的，
	有个缺陷，当最后一个+-符号不是连接实数根虚数的部分时，会报错，比如 -7.2e+4-5.23e-8j
	不过整体思路挺好的
	'''
	if 'j' not in _str:  # 处理只有实数的情况
		return complex(float(_str))
	else:
		_str_no_blank = ''.join(_str.split())  # 把输入可能带入的空格去除
		comlist = _str_no_blank.split('j')
		if '' not in comlist:  # 处理虚数在前，实数在后的情况
			return complex(float(comlist[1]), float(comlist[0]))
		else:
			length = len(_str)
			_index = 0
			for i in range(-1, -length, -1):
				if _str[i] in ('+', '-'):
					_index = i
					break
			return complex(float(_str[:_index]), float(_str[_index:-1]))


if __name__ == '__main__':
	print atoc(raw_input('Enter a integer: '))
