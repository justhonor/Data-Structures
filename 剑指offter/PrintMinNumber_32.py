#!/usr/bin/python
# coding:utf-8
##
# Filename: PrintMinNumber_32.py
# Author  : aiapple
# Date    : 2017-08-15
# Describe: 剑指offter NO.32
#           
#           输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
#       打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
#       则打印出这三个数字能排成的最小数字为321323。
################################################
 # * 解题思路：
 # * 先将整型数组转换成String数组，然后将String数组排序，最后将排好序的字符串数组拼接出来。关键就是制定排序规则。
 # * 排序规则如下：
 # * 若ab > ba 则 a > b，
 # * 若ab < ba 则 a < b，
 # * 若ab = ba 则 a = b；
 # * 解释说明：
 # * 比如 "3" < "31"但是 "331" > "313"，所以要将二者拼接起来进行比较
def PrintMinNumber(numbers):
	if not numbers:
		return " "

	lmb = lambda n1,n2:int(str(n1)+str(n2))-int(str(n2)+str(n1))
	array = sorted(numbers,cmp=lmb)

	return ''.join([str(i) for i in array])

n = [3,32,321]

print PrintMinNumber(n)