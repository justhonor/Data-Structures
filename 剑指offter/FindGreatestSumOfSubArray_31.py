#!/usr/bin/python
# coding:utf-8
##
# Filename: FindGreatestSumOfSubArray_31.py
# Author  : aiapple
# Date    : 2017-08-15
# Describe: 剑指offter NO.31
#           
#		    求连续子向量的最大和(子向的长度最少为1)
#       例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)
##
################################################

def FindGreatestSumOfSubArray(array):
    # write code here
    max = -100000
    curSum = 0
    
    for i in range(len(array)):
        if curSum < 0:
            curSum = array[i]
        else:
            curSum += array[i]
            
        if curSum > max:
            max = curSum
    
    return max

#a = [1,-2,3,10,-4,7,2,-5]
a = [-2,-8,-1,-5,-9]

print FindGreatestSumOfSubArray(a)