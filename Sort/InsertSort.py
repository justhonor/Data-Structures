#!/usr/bin/python
# coding:utf-8
##
# Filename: InsertSort.py
# Author  : aiapple
# Date    : 2017-07-06
# Describe:
##
#############################################

def insertSort(A):
    length = len(A)
    i = 1
    while(i<length):
        temp = A[i]
        j = i-1
        while  j>=0 and A[j]>temp:
            A[j+1] = A[j]
            j = j-1

        A[j+1] = temp
        i=i+1

a=[54,35,48,36,27,12,44,44,8,14,26,17,28];
print "input array:%s"%a
insertSort(a)
print "output array:%s"%a

