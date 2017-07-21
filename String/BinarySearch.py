#!/usr/bin/python
# coding:utf-8
##
# Filename: BinarySearch.py
# Author  : aiapple
# Date    : 2017-07-21
# Describe: 二分法查找
#           
#           递归和非递归方式
##
#############################################
import time

def TCT(times):
    def TimeCost(f):
        def _f(*args,**kargs):
            mine = 10000
            sume = 0
            for t in range(times):
                start = time.time()
                a = f(*args,**kargs)
                end = time.time()
                if mine > end-start:
                    mine = end-start
                sume = sume + (end-start)
            print f.__name__ + "平均耗时:",sume/times
            print f.__name__ + "最少耗时:",mine
        return _f
    return TimeCost

@TCT(100)
def BinarySearch(List,key):
    lenth = len(List)
    left = 0 
    right = lenth-1

    while(left <= right):
        mid = (left + right)/2
        if key == List[mid]:
            print  "BS 找到%s 下标:%s"%(key,mid)
            return True
        elif key > List[mid]:
            left = mid + 1
        else:
            right = mid - 1

    print "BS 没有找到",key

# 注意right 是下标不是长度
#@TCT(100)
def BinarySearch_Recur(List,key,left,right):
    mid = (left + right) / 2
    if left > right:
        print "RRRR 没有找到",key
        return False
    if key == List[mid]:
        print  "RRRR 找到%s 下标:%s"%(key,mid)
        return True
    elif key > List[mid]:
        left = mid + 1
        return BinarySearch_Recur(List,key,left,right)
    else:
        right = mid - 1
        return BinarySearch_Recur(List,key,left,right)



L1 = [1,2,3,4,5,6,7,8,9,12,13,45,67,89,99,101,111,123,134,565,677]
#L1 = [1,2,3,4,5,6,7,8,9]

BinarySearch_Recur(L1,111,0,len(L1)-1)
#BinarySearch(L1,111)


