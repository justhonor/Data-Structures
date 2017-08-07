#!/usr/bin/python
# coding:utf-8
##
# Filename: HasSubtree_18.py
# Author  : aiapple
# Date    : 2017-08-7
# Describe: 剑指offter NO.18
#           
#		输入两棵二叉树A，B，判断B是不是A的子结构。
#		（ps：我们约定空树不是任意一个树的子结构）
##
#############################################
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    
    def DoesTree1HaveTree2(self,t1,t2):
        
        # t2 结束还没有发现不同，则true
        if t2 == None:
            return True
        
        # t1已结结束，t2还没有结束，则False
        if t1 == None:
            return False
        
        # 子树中有不相同则 false
        if t1.val != t2.val:
            return False
        
        if self.DoesTree1HaveTree2(t1.left,t2.left) and self.DoesTree1HaveTree2(t1.right,t2.right):
            return True
        else:
            return False
        # return self.DoesTree1HaveTree2(t1.left,t2.left) && self.DoesTree1HaveTree2(t1.right,t2.right);
        
    
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        
        if pRoot1 == None:
            return result
        
        if pRoot2 == None:
            return result
        
        # 找到与t2根节点值相同的节点
        if pRoot1.val == pRoot2.val:
            result = self.DoesTree1HaveTree2(pRoot1,pRoot2)
            
        if result == False:
            result = self.HasSubtree(pRoot1.left,pRoot2)
        if result == False:
            result = self.HasSubtree(pRoot1.right,pRoot2)
            
        return result
            
        