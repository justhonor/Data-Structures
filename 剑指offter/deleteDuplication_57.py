#!/usr/bin/python
# coding:utf-8
##
# Filename: deleteDuplication_57.py
# Author  : aiapple
# Date    : 2017-08-18
# Describe: 剑指offter NO.57
#           
#    	在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
#   重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
##
################################################

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return 
        
        prevV = -1
        if pHead.val == -1:
            prevV = -2
            
        Prev = ListNode(prevV)
        Prev.next = pHead
        
        prev = Prev
        
        while pHead and pHead.next:
            if pHead.val == pHead.next.val:
                val = pHead.val
                while pHead and pHead.val==val:
                    pHead = pHead.next
                prev.next = pHead
            else:
                prev = pHead
                pHead = pHead.next
                
        return Prev.next
