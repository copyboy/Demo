# -*- coding:utf-8 -*-
__author__ = 'Yuriy'

'''
6–15.转换
(a)给出两个可识别格式的日期,比如 MM/DD/YY 或者 DD/MM/YY 格式,计算出两个日期间的天
数.
(b)给出一个人的生日,计算从此人出生到现在的天数,包括所有的闰月.
(c)还是上面的例子,计算出到此人下次过生日还有多少天.
	解：难点在（a）, MM/DD/YY 或者 DD/MM/YY 格式 只需要识别一个就行，不要纠结实现两种格式
	使用 DD/MM/YY，年先比较，大的减去小的，如果相等，比较月份，再相等，比较日
	月份，可能是大的月份减去小的月份，但也有可能是大月份到小月份
	日，跟月相同。
	还有个闰年的问题，包含2月份、在2月，区分开
	不要直接想最优解，先试着完成题目！

'''
import time


def isLeapYear(year):
	if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
		return True


def IntervalDays(str1, str2):
	month1 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	month2 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	# 假定输入的日期都是正确的且后一个日期比前一个日期大
	bdate = str1.split('/')
	bdate[0], bdate[1], bdate[2] = int(bdate[0]), int(bdate[1]), int(bdate[2])
	edate = str2.split('/')
	edate[0], edate[1], edate[2] = int(edate[0]), int(edate[1]), int(edate[2])
	if bdate == edate:
		print '0 days'
	elif bdate[1] == edate[1] and bdate[2] == edate[2]:
		print '%d days' % abs(bdate[0] - edate[0])
	elif bdate[1] != edate[1] and bdate[2] == edate[2]:
		bdays = 0
		edays = 0
		if isLeapYear(bdate[2]):
			for i in range(1, bdate[1]):
				bdays += month2[i]
			bdays = bdays + bdate[0]
			for i in range(1, edate[1]):
				edays += month2[i]
			edays = edays + edate[0]
			print '%d days' % abs(edays - bdays)
		else:
			for i in range(1, bdate[1]):
				bdays += month1[i]
			bdays = bdays + bdate[0]
			for i in range(1, edate[1]):
				edays += month1[i]
			edays = edays + edate[0]
			print '%d days' % abs(edays - bdays)
	elif bdate[2] != edate[2]:
		days = 0
		for i in range(bdate[2] + 1, edate[2]):
			if isLeapYear(i):
				days += 366
			else:
				days += 365
		if isLeapYear(bdate[2]):
			for i in range(bdate[1] + 1, 13):
				days += month2[i]
			days += (month2[bdate[1]] - bdate[0])
		else:
			for i in range(bdate[1] + 1, 13):
				days += month1[i]
			days += (month1[bdate[1]] - bdate[0])
		if isLeapYear(edate[2]):
			for i in range(1, edate[1]):
				days += month2[i]
			days += edate[0]
			print '%d days' % (days)
		else:
			for i in range(1, edate[1]):
				days += month1[i]
			days += edate[0]
			print '%d days' % (days)


if __name__ == '__main__':
	# (a)
	date1 = raw_input("input a start date as DD/MM/YYYY: ")
	date2 = raw_input("input a end date as DD/MM/YYYY: ")
	IntervalDays(date1, date2)
	#(b)
	birth = raw_input("input a birth date as DD/MM/YYYY: ")
	today = str(time.strftime("%d/%m/%Y"))
	print 'today is %s ' % today
	IntervalDays(birth, today)
	#(c)
	birth = raw_input("input a birth date as DD/MM/YYYY: ")
	today = str(time.strftime("%d/%m/%Y"))
	print 'today is %s ' % today
	if today.split('/')[1] < birth.split('/')[1]:
		nbirth = str(birth.split('/')[0] + '/' + birth.split('/')[1] + '/' + today.split('/')[2])
		IntervalDays(today, nbirth)
	elif today.split('/')[1] == birth.split('/')[1]:
		if today.split('/')[0] < birth.split('/')[0]:
			print '%d days' % (int(birth.split('/')[0]) - int(today.split('/')[0]))
		else:
			year = int(today.split('/')[2]) + 1
			nbirth = str(birth.split('/')[0] + '/' + birth.split('/')[1] + '/' + str(year))
			IntervalDays(today, nbirth)