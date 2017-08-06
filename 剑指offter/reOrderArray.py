#!/usr/bin/python
# coding:utf-8
##
# Filename: reOrderArray.py
# Author  : aiapple
# Date    : 2017-08-6
# Describe: 剑指offter NO.11
#           
#		输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
#	使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
#   并保证奇数和奇数，偶数和偶数之间的相对位置不变。
##
#############################################
def reOrderArray(array):
	qi = 0 # 奇数索引位置
	for i in range(len(array)):
		if array[i] % 2 == 1:
			array.insert(qi,array.pop(i))
			qi += 1

	return array

a = [1,2,3,4,5,6,7,8,9]

print reOrderArray(a)
