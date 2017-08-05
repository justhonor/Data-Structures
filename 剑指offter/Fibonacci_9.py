#!/usr/bin/python
# coding:utf-8
##
# Filename: minNumberInRotateArray.py
# Author  : aiapple
# Date    : 2017-08-5
# Describe: 剑指offter NO.9
#           
#		大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
#	n<=39大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
#	n<=39
##
#############################################

def Fibonacci(n):
    # write code here
    result = [0,1]
    
    if n < 0:
        return False
    
    if n < 2:
        return result[n]
    
    fib1 = 0
    fib2 = 1
    
    for i in range(2,n+1):
        fibN = fib1 + fib2
        fib1 = fib2
        fib2 = fibN
    
    return fibN
print Fibonacci(39)

# def fib_iter():
#     a,b = 0,1
#     yield a
#     while True:
#         yield b
#         a,b = b,a+b

# A = fib_iter()
# iter_result= [A.next() for i in xrange(40)]
# print iter_result
