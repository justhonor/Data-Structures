#!/usr/bin/python
# coding:utf-8
##
# Filename: FindFirstCommonNode_37.py
# Author  : aiapple
# Date    : 2017-08-16
# Describe: 剑指offter NO.37
#
#		   输入两个链表，找出它们的第一个公共结点
##
################################################

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 is None or pHead2 is None:
            return 
        
        ph = {}
        p1 = pHead1
        p2 = pHead2
        while p1:
            if not ph.has_key(p1.val):
                ph[p1.val] = p1.val
            p1 = p1.next
            
        while p2:
            if ph.has_key(p2.val):
                return p2
            p2 = p2.next
            
        return


