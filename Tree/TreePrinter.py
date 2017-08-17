#!/usr/bin/python
# coding:utf-8
##
# Filename: TreePrinter.py
# Author  : aiapple
# Date    : 2017-07-24
# Describe: 按行打印二叉树
#           层次遍历,每层占一行打印
##
#############################################
class Node(object):
	"""docstring for Node"""
	def __init__(self, elem=-1,lchild=None,rchild=None):
		super(Node, self).__init__()
		self.elem = elem
		self.lchild = lchild
		self.rchild = rchild

class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		super(Tree, self).__init__()
		self.root = Node()

	def treeAdd(self,elem):
		"""给树增加节点"""

		node = Node(elem)
		if self.root.elem == -1: # 树为空
			self.root = node
			return self.root

		myqueue = []
		myqueue.append(self.root)
		while myqueue:
			cur = myqueue.pop(0)
			print "当前节点值:%s"%cur.elem
			if cur.lchild is None:
				print "%s 增加在左孩子上"%elem
				cur.lchild = node
				return self.root
			elif cur.rchild is None:
				print "%s 增加在右孩子上"%elem
				cur.rchild = node
				return self.root
			else:
				print "当前节点值:%s 已经有左右孩子"%cur.elem
				myqueue.append(cur.lchild)
				myqueue.append(cur.rchild)

	def treePrinter(self,root):
		"""
			按层打印二叉树
			last:正在打印的当前行的最右节点
				 打印的节点cur = last 该换行列,last = nlast
			nlast:表示最新加入的节点(即下一行的最右节点), myqueue.append(cur) nlast = cur,
		"""
		myqueue=[]
		last = root
		myqueue.append(root)
		string = ""
		while myqueue:
			cur = myqueue.pop(0)
			string += str(cur.elem)

			if cur.lchild is not None:
				myqueue.append(cur.lchild)
				nlast = cur.lchild
			
			if cur.rchild is not None:
				myqueue.append(cur.rchild)
				nlast = cur.rchild

			# 打印的节点是该行最右的节点
			if cur == last:
				string += "\n"
				last = nlast

		print  "按层打印二叉树:\n",string

if __name__ == '__main__':
	
	elems = range(1,9)
	tree = Tree()

	for elem in elems:
		tree.treeAdd(elem)

	tree.treePrinter(tree.root)









		
		