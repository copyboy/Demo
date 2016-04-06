# -*- coding:utf-8 -*-
__author__ = 'Yuriy'

'''
6–14.随机数.设计一个"石头,剪子,布"游戏,有时又叫"Rochambeau",你小时候可能玩过,下面
是规则.你和你的对手,在同一时间做出特定的手势,必须是下面一种手势:石头,剪子,布.胜利者从
下面的规则中产生,这个规则本身是个悖论.
(a)布包石头.
(b)石头砸剪子,
(c)剪子剪破布.在你的计算机版本中,用户输入她/他的选项,计算机找一个随机选项,然后由你
的程序来决定一个胜利者或者平手.注意:最好的算法是尽量少的使用 if 语句.
	解：随机数生成1,2,3 ，分别对应不同的手势。定义函数，用户输入的跟随机生成的比较大小
		少用if，该怎么比较？一共3*3种结果，直接列出来在字典里就行
		结果：获胜、平局、输
'''

import random


def gameOne(ch):
	# 1是人输入 2是随机数据

	msg = {1: '剪刀', 2: '石头', 3: '布'}
	print '你出了%s' % msg[ch]
	ms = {'11': 'Draw', '12': 'Lose', '13': 'Win', '21': 'Win', '22': 'Draw', '23': 'Lose', '31': 'Lose', '32': 'Win',
	      '33': 'Draw'}
	compu = random.randint(1, 3)
	print '电脑出了%s' % msg[ch]
	li = str(ch) + str(compu)
	print '结果：你%s, 再来一次' % ms[li]


def main():
	print '''石头剪刀布
		1.剪刀
		2.石头
		3.布
		请输入你的选择:
	'''
	while True:

		try:
			ch = int(raw_input())
		except Exception:
			continue
		if ch in [1, 2, 3]:
			gameOne(ch)
		else:
			print '输入错误，请重新输入'
			continue

if __name__ == '__main__':
	main()
