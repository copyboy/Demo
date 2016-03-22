# coding:utf-8
__author__ = 'Yuriy'

'''
5-14 银行利息。写一个函数，以定期存款利率为参数， 假定该账户每日计算复利，请计
算并返回年回报率。
难怪复利是违法的，这样每天算复利也太bug了。。。
'''

def yearReward(x):
	return (1 + x) ** 365

def show():

	ch = float(raw_input('输入定期存款利率：'))
	print '年利率为 %.2f' % yearReward(ch)

if __name__ == '__main__':
	show()

# dayrate=float(raw_input("input a rate "))
# print 'a year rate of earn is %f' %((1+dayrate)**365-1)