#!/usr/bin/python
# coding:utf-8
##
# Filename: Power_11.py
# Author  : aiapple
# Date    : 2017-08-6
# Describe: 剑指offter NO.11
#           
#		给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
##
#############################################
def Power(base, exponent):
    # write code here
    if base - 0 < 0.000001 and base - 0 >0.00000000001:
        return 0
    
    result = 1
    if exponent == 0 :
        return 1
    elif exponent > 0 :
        for i in range(exponent):
            result = result * base
        return result 
    elif exponent <0:
        E = abs(exponent)
        for i in range(E):
            result = result *base
        return 1.0/result

print Power(-2,3)