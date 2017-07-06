#!/usr/bin/python
# coding:utf-8
##
# Filename: SelectionSort.py
# Author  : aiapple
# Date    : 2017-07-06
# Describe:
##
#############################################

def selectionSort(A):
    length = len(A)
    i = 0
    while (i<length-1):
        min = i
        for j in range(i+1,length):
            if A[j] < A[min]:
                min = j
        if min != i:
            temp=A[min]
            A[min]=A[i]
            A[i]=temp
        i=i+1

a  = [2,14,17,9,8,16]
print "input array:%s"%a
selectionSort(a)
print "output array:%s"%a
