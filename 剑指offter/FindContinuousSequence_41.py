#!/usr/bin/python
# coding:utf-8
##
# Filename: FindContinuousSequence_41.py
# Author  : aiapple
# Date    : 2017-08-17
# Describe: 剑指offter NO.41
#
#		   和为S的两个数字  VS  和为S的连续正数序列
##
################################################
def FindContinuousSequence(tsum):
    # write code here
    if tsum < 3:
        return []
    small = 1
    big = 2
    middle = tsum + 1 / 2
    res = []
    while small < middle and small < big:
        curSum = (small + big)*(big-small+1)/2
        if curSum == tsum:
            res.append([i for i in range(small,big+1)])
            # big += 1
            small += 1
        elif curSum < tsum:
            big += 1
        else:
            small += 1
            
    return res

def FindNumbersWithSum(self, array, tsum):
    # write code here
    if tsum < 2:
        return []
    
    small = 0
    big = len(array)-1
    res = []
    while small < big:
        curSum = array[small] + array[big]
        if curSum == tsum:
            res.append(array[small])
            res.append(array[big])
            big -= 1
            return res
        elif curSum > tsum:
            big -= 1
        else:
            small += 1
        
    return []