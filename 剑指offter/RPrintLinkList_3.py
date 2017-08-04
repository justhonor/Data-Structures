#!/usr/bin/python
# coding:utf-8
##
# Filename: RPrintLinkList_3.py
# Author  : aiapple
# Date    : 2017-08-4
# Describe: 剑指offter NO.3
#           
# 			输入一个链表，从尾到头打印链表每个节点的值。
##
#############################################
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def printListFromTailToHead(self, listNode):
	cur = listNode
	vals = []
	while cur.next is not None:
		vals.append(cur.val)
		cur = cur.next

	vals.append(cur.val)


	for i in vals.reverse():
		print i 
