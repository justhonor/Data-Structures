# coding:utf-8
##
# Filename: PrintMinNumber_35.py
# Author  : aiapple
# Date    : 2017-08-15
# Describe: 剑指offter NO.35
#           
#          在一个字符串(1<=字符串长度<=10000，全部由字母组成)
#        中找到第一个只出现一次的字符,并返回它的位置
################################################
def FirstNotRepeatingChar(s):
    if not s:
        return -1
    
    ones={}
    for i in range(len(s)):
        if ones.has_key(s[i]):
            ones[s[i]] += 1
        else:
            ones[s[i]] = 1
    
    for i in range(len(s)):
        if ones[s[i]] == 1:
            return i


s = 'google'
s.find
print FirstNotRepeatingChar(s)

