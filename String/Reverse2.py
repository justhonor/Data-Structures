#!/usr/bin/python
# coding:utf-8
##
# Filename: Reverse2.py
# Author  : aiapple
# Date    : 2017-07-21
# Describe: 递归实现字符串逆序
##
#############################################

def reverse_r(string):
    if len(string) <= 1:
        return string
    else:
        return reverse_r(string[1:]) + string[0]

word = "i like python "

print reverse_r(word)
