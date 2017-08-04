#!/usr/bin/python
# coding:utf-8
##
# Filename: FindNumInArray.py
# Author  : aiapple
# Date    : 2017-08-4
# Describe: 剑指offter NO.1
#           
#    在一个二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
##
#############################################
def Find(target, array):
     # 遍历每一行,每行使用二分法查找
    for i in range(len(array)):
     	line = array[i]
        # write code here
        length = len(line)
        left = 0
        right = length - 1
        
        while left<=right:
            mid = (left+right)/2
            if target == line[mid]:
            	print "find target:%s"%target
                return True
            elif target > line[mid]:
            	left = mid + 1
            elif target < line[mid]:
            	right = mid -1
    print "no"
    return False





a = [[1,2,3],[4,6,8],[10,11,15]]
Find(88,a)