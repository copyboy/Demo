# -*- coding:utf-8 -*-
__author__ = 'Yuriy'

'''
6–8. 列表.给出一个整数值,返回代表该值的英文， 比如输入 89 返回"eight-nine"。 附加题：
能够返回符合英文语法规则的形式，比如输入“89”返回“eighty-nine” 。本练习中的值限定在家 0
到 1,000.
'''
#
# def form(ch):
# 	# msg = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
# 	num = range(10)
# 	num_x = [str(x) for x in num]
# 	num_str = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# 	msg = dict(zip(num_x, num_str))
#
# 	length = len(ch)
# 	# print length
# 	# print msg
# 	li = []
# 	for i in ch:
# 		li.append(msg[i])
# 	print li
# 	print '-'.join(li)
#
#
# if __name__ == '__main__':
# 	ch = raw_input('input a number:')
# 	form(ch)


# 附加题：这是从网上直接找的答案，字典太大就不想写 ~~~~(>_<)~~~~ 最大数值到1000
dict1 = {"1" :"one" , "2" : "two" , "3" : "three" , "4" : "four" , "5" : "five" ,"6" : "six", "7" : "seven" , "8" : "eight" , "9" : "nine", "0" : "" }
dict2 = {"1" :"ten" , "2" : "twenty" , "3" : "thirty" , "4" : "forty" , "5" : "fifty" ,"6" : "sixty", "7" : "seventy" , "8" : "eighty" , "9" : "ninety", "0" : "" }
dict3 = {"1" :"one hundred" , "2" : "two hundred" , "3" : "three hundred" , "4" : "four hundred" , "5" : "five hundred" ,"6" : "six hundred", "7" : "seven hundred" , "8" : "eight hundred" , "9" : "nine hundred", "0" : "" }
dictAll = {1: dict1 , 2:dict2 , 3: dict3}
def fun(strNum):
  if int(strNum)>1000 or int(strNum)<0:
    return "Invalid Number, Please input again"
  length = len(strNum)
  strTemp = ""
  if len(strNum) == 4:
    strTemp = "One Thousand"
    return strTemp
  for i in range(length):          # 这个二维的字典，有点巧妙
    strTemp += dictAll[length - i][strNum[i]] +" "
  return strTemp

if __name__ == "__main__":
  while True:
    strNum = raw_input("请输入一个数字，按q退出:")
    if strNum.lower() == 'q' :
      break
    print fun(strNum)