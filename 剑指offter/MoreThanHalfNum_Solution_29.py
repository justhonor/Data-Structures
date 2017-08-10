#!/usr/bin/python
# coding:utf-8
##
# Filename: MoreThanHalfNum_Solution_29.py
# Author  : aiapple
# Date    : 2017-08-10
# Describe: 剑指offter NO.29
#           
#		数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
#     例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，
#     超过数组长度的一半，因此输出2。如果不存在则输出0。
##
#############################################
def MoreThanHalfNum_Solution(numbers):
        # write code here
        if len(numbers) ==1:
        	return numbers[0]

        numTimes = {}
        num = len(numbers)/2
        
        for n in numbers:
            if numTimes.has_key(n):
                numTimes[n] += 1
                if numTimes[n] > num:
                    return n
            else:
                numTimes[n] = 1
        return 0

numbers = [1,2,3,2,2,2,5,4,2]
print MoreThanHalfNum_Solution(numbers)