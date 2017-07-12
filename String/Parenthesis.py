#!/usr/bin/python
# coding:utf-8
##
# Filename: Parenthesis.py
# Author  : aiapple
# Date    : 2017-07-12
# Describe: 合法括号序
##            判断一个字符串是否未合法的括号串
#           "((a))" --> True
#           ")(()"  --> Flase
#############################################

def chkParenthesis(string):
    number = 0;
    for i in range(len(string)):
        if string[i] == "(":
            number = number + 1
        if string[i] == ")":
            number = number - 1
        if number < 0 :         # 保证左括号数量不小于又括号
            return False
    if number == 0 :
        return True
    else:
        return False


if __name__=="__main__":
    string = "())a()"
    print "input string:%s"%string 
    print "The result is :%s"%chkParenthesis(string)
