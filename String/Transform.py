#!/usr/bin/python
# coding:utf-8
##
# Filename: Transform.py
# Author  : aiapple
# Date    : 2017-07-10
# Describe: 变形词判断 
#               对于两个字符串A和B,如果A和B中出现的字符种类相同且
#          每种字符出现的次数相同,则A和B互为变形词       
##         给定两个字符串A和B及他们的长度,判断他们是否为变形词
################################################################## 

def chkTansform(A,B):

    if len(A) != len(B):
        return False 

    length = len(A)
    dicA={}
    dicB={}
    # 用字典统计个字符的个数
    for i in range(length):
        if dicA.has_key(A[i]):
            dicA[A[i]]=dicA[A[i]]+1
        else:
            dicA[A[i]]=1
        if dicB.has_key(B[i]):
            dicB[B[i]]=dicB[B[i]]+1
        else:
            dicB[B[i]]=1

    # A字典中的key B字典中没有 则false,有值不等 也是false 
    for key in dicA.iterkeys():
        if dicB.has_key(key):
            if dicA[key] == dicB[key]:
                continue
            else:
                return False
        else:
            return False
    return True 

if __name__=='__main__':

    A = "abce"
    B = "ebac"
    print chkTansform(A,B)

