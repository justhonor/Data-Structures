#!/usr/bin/python
# coding:utf-8
##
# Filename: FindKthToTail_13.py
# Author  : aiapple
# Date    : 2017-08-6
# Describe: 剑指offter NO.13
#           
#		输入一个链表，输出该链表中倒数第k个结点。
##
#############################################

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None:
            return 
        
        values = []
        cur = head
        while cur!=None:
            values.append(cur)
            cur = cur.next
        
        if len(values) < k or k<1:
            return 
        return values[-k]