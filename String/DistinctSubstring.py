#!/usr/bin/python
# coding:utf-8
##
# Filename: DistinctSubstring.py
# Author  : aiapple
# Date    : 2017-07-12
# Describe: 最长无重复子串
##              找到最长无重复子串
#               "aabcd" --> "abc"
#               "abc"   --> "abc"
#############################################

def DistinctSubstring(string):
    # 找到以每个字符结束时的最长无重复子串
    # 在这些子串中找到最长的即可

    # dic 记录每个字符上次出现的位置
    strPosition = {}

    # 记录以每个字符结束时的最长无重复字串
    # Dsub = []
    Dsub = ""

 
    # 用于查找字串中的重复字符的位置
    subnum = {}
    for i in range(len(string)):
        # 获取上次出现的位置,未出现过pos=0
        if not strPosition.has_key(string[i]):
            strPosition[string[i]] = i
            pos = -1
        else:
            pos = strPosition[string[i]]
    
        posI = pos + 1 # i位置的最长无重复字串的起始位置

        # 找出子串中重复的偏移量
        for j in range(posI,i):
            if not subnum.has_key(string[j]):
                subnum[string[j]]=j
            else:
                # 有重复,posI等于该字符上次出现位置之后一位
                if posI < j:
                    posI = subnum[string[j]] + 1 
                
                # 更新位置
                subnum[string[j]]=j

        if len(string[posI:i+1]) > len(Dsub):
            Dsub = string[posI:i+1]
        # Dsub.append(string[posI:i+1])
        subnum = {}
        posI = 0
    
    
    return Dsub

if __name__=="__main__":
    string = "aabcccertytyfsmusd"
    print "input  string:%s"%string
    print "output string:%s"%DistinctSubstring(string)
