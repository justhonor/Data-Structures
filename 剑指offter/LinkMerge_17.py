#!/usr/bin/python
# coding:utf-8
##
# Filename: LinkMerge_17.py
# Author  : aiapple
# Date    : 2017-08-7
# Describe: 剑指offter NO.17
#           
#		输入两个单调递增的链表，输出两个链表合成后的链表，
#    当然我们需要合成后的链表满足单调不减规则。
##
#############################################
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None and pHead2 != None:
            return pHead2
        elif pHead2 == None and pHead1 != None:
            return pHead1
        elif pHead1 == None and pHead2 == None:
            return None
        
        merged = ListNode(-1)
        p  = merged
        
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                merged.next = pHead1
                pHead1 = pHead1.next
            else:
                merged.next = pHead2
                pHead2 = pHead2.next
            
            merged = merged.next
                
        
        # 没有结束则将没有结束的链起来
        if pHead1:
            merged.next = pHead1
        
        if pHead2:
            merged.next = pHead2
            
        return  p.next