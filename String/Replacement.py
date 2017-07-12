#!/usr/bin/python
# coding:utf-8
##
# Filename: Replacement.py
# Author  : aiapple
# Date    : 2017-07-12
# Describe: 空格替换
##              将字符串中的所有的空格替换成%20
#           "l am a student." --> l%20am%20a%20students.
#
#########################################################

def replacement(string):
    nString = ""
    for i in range(len(string)):
        if string[i] == " ":
            nString = nString + "%20"
        else:
            nString = nString + string[i]
    
    return nString 


if __name__=="__main__":
    string = "Hello  Word ! "
    print "input string:%s"%string
    print "output strting:%s"%replacement(string)
