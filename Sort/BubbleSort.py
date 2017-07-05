#!/usr/bin/python
# coding:utf-8
##
# Filename: BubbleSort.py
# Author  : aiapple
# Date    : 2017-07-05
# Describe:
##
#############################################

def BubbleSort(a):
    length = len(a)
    while(length):
        for j in range(length-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
        length=length-1
    print "output array:%s"%a

if __name__ == '__main__':
    a  = [2,14,17,9,8,16]
    print "input array:%s"%a
    BubbleSort(a)
