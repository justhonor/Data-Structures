#!/usr/bin/python
# coding:utf-8
##
# Filename: LastRemaining_Solution_45.py
# Author  : aiapple
# Date    : 2017-08-17
# Describe: 剑指offter NO.45
#
#		   圆圈中最后剩下的数字
##
################################################

def LastRemaining_Solution(n, m):
    # write code here
    if not n or not m:
        return 
    
    res = [i for i in range(n)]
    start = 0
    while len(res) != 1:
        p = (start+m-1)%n
        print "number:%s pop:%s"%(p,res.pop(p))
        # res.pop(p)
        n -= 1
        start = p
    
    print res
    return res[0]

LastRemaining_Solution(5,3)