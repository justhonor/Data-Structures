#!/usr/bin/python
# coding:utf-8
##
# Filename: Mirror_19.py
# Author  : aiapple
# Date    : 2017-08-7
# Describe: 剑指offter NO.19
#           
#		操作给定的二叉树，将其变换为源二叉树的镜像。
##
#############################################
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return
        cur = root
        
        mq = []
        mq.append(cur)
        
        # 层次遍历，如果是非页子节点则，将其左右字树调换
        while mq:
            cur=mq.pop(0)
            if cur.left:
                mq.append(cur.left)
            if cur.right:
                mq.append(cur.right)
            
            # 判断是为叶子节点
            if cur.left or cur.right:
                cur.left,cur.right = cur.right,cur.left
            
            
            
            
