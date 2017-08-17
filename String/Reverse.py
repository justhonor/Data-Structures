#!/usr/bin/python
# coding:utf-8
##
# Filename: Reverse.py
# Author  : aiapple
# Date    : 2017-07-10
# Describe: 句子逆序
#           "dog loves pig" --> "pig loves dog"
#           "l am a student." --> "student. a am l"
##
#############################################
import pdb
def reverseSentence(String):

    # 对句子整体逆序
    rString = reverseWord(String)

    reversedString = ""
    # 对已逆序句子中的单词再逆序得到结果
    # pdb.set_trace()
    for word in rString.split():
        reversedString = reversedString + reverseWord(word) + " "

    print "ssdf",reversedString
    return reversedString.rstrip()

# 递归求反
def reverseWord(word):
    
    if len(word) <= 1:
        return word
    else:
        return reverseWord(word[1:]) + word[0]

'''
def reverseWord(word):

    Word = list(word)
    # 奇偶数长度选择
    if len(Word)%2:
        clength = len(Word)/2
    else:
        clength = len(Word)/2 + 1

    for i in range(clength):
        temp = Word[i]
        j = i + 1
        Word[i] = Word[-j]
        Word[-j] = temp

    return "".join(Word)
'''        

if __name__=="__main__":

    string1 = "dog loves pig"
    string2 = "l am a student."

    S = string1
    print "input %s"%S
    rstring = reverseSentence(S)
    # rstring = reverseWord(S)
    print "output %s"%rstring
