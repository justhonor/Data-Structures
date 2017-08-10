#!/usr/bin/python
# coding:utf-8
##
# Filename: MoreThanHalfNum_Solution_30.py
# Author  : aiapple
# Date    : 2017-08-10
# Describe: 剑指offter NO.30
#           
#		输入n个整数，找出其中最小的K个数。
#       例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
##
#############################################
def GetLeastNumbers_Solution(tinput, k):
    # write code here
    if k <=0:
        return False
    
    if len(tinput) < k:
        return False
    
    minK = []
    maxI = -1
    for i in tinput:
        if len(minK) < k:
            minK.append(i)
        elif len(minK) == k:
        	# print minK
        	minK.sort()
        	for j in range(k-1,-1,-1):
        		if minK[j] > i:
        			minK[j] = i
        			break;
    return minK
l = [4,5,1,6,2,7,3,8]
k = 4

print GetLeastNumbers_Solution(l,k)