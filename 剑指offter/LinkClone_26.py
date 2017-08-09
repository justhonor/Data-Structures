#!/usr/bin/python
# coding:utf-8
##
# Filename: LinkClone_26.py
# Author  : aiapple
# Date    : 2017-08-9
# Describe: 剑指offter NO.26
#           
#		输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
#       另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
#      （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
##
#############################################
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return
        # 链表复制节点，跟在源节点之后
        cur  = pHead
        while cur:
            tmp = RandomListNode(cur.label)
            tmp.next = cur.next
            tmp.random = None
            cur.next = tmp
            
            cur = tmp.next
        
        # 如果源节点有random，复制节点的random 即在源节点random之后一位
        cur = pHead
        while cur:
            tmp = cur.next
            if cur.random: tmp.random = cur.random.next
            cur = tmp.next
        
        # 将原节点与复制节点分离
        # 每个节点均指向后面第二个节点
        cur = pHead
        res = pHead.next
        while cur.next:
            tmp = cur.next
            cur.next = tmp.next
            cur = tmp
        return res
            