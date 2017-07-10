#!/usr/bin/python
# coding:utf-8
##
# Filename: Rotation.py
# Author  : aiapple
# Date    : 2017-07-10
# Describe: 旋转词判断
##              字符串A,将A的前面任意部分移动到后边形成的字符串为A的旋转词
#          如A="1234",旋转词有 "1234","4321","3412","2341"
#                判断两字符串是否为旋转词
##########################################################################

def chkRotation(A,B):

    if len(A) != len(B):
        return False

    # 将A字符串相加组成大字符串C,此时C中拥有A所有旋转词的集合
    # 判断B是否未c中子串即可 
    C = A + A
    if C.find(B) == -1:
        return False
    return True

    

if __name__=="__main__":

    A = "12345"
    #B = "23451"
    B = "34521"
    print chkRotation(A,B)

