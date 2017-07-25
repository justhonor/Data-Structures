#!/usr/bin/python
# coding:utf-8
##
# Filename: TreeToString.py
# Author  : aiapple
# Date    : 2017-07-24
# Describe: 二叉树序列化与反序列化
##          序列化与反序列化使用统一遍历方式
#			如 先序遍历
#############################################
class Node(object):
	"""docstring for Node"""
	def __init__(self,elem=-1,lchild=None,rchild=None):
		self.elem = elem
		self.lchild = lchild
		self.rchild = rchild


class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		self.root = Node()
		# 序列化字符串
		self.string = ""

	def TreeAdd(self,elem):
		"""给树增加节点,按层增加"""
		node = Node(elem)
		if self.root.elem == -1:
			self.root = node
			return self.root

		myqueue = []
		myqueue.append(self.root)
		while myqueue:
			cur = myqueue.pop(0)
			# print "当前节点值:%s"%cur.elem
			if cur.lchild is  None:
				# print "%s 增加在左孩子上"%elem
				cur.lchild = node
				return self.root
			elif cur.rchild is None:
				# print "%s 增加在右孩子上"%elem
				cur.rchild = node
				return self.root
			else:
				# print "当前节点值:%s 已经有左右孩子"%cur.elem
				myqueue.append(cur.lchild)
				myqueue.append(cur.rchild)

	# 使用递归先序遍历,进行序列化
	def TreeToStringRecur(self,root):
		"""
			二叉树序列化
			每个节点以!结尾,空节点用#!表示
		"""
		if root is None:
			self.string +="#!"
			return 
		self.string +="%s!"%root.elem
		self.TreeToStringRecur(root.lchild)
		self.TreeToStringRecur(root.rchild)
    

def StringToTree(node,stringList):
	""" 先序遍历的反序列化
		['1', '2', '4', '8', '#', '#', '#', '5', '#', '#', '3', '6', '#', '#', '7', '#', '#']
		1. 弹出队列值,作为节点值
		2. 剩余队列,创建该节点的左右子树.
		3. 首先创建左子树,直到空节点"#",再创建右子树直到"#" 为止
	"""
	if len(stringList) == 0:
		return

	node.elem = stringList.pop(0)
	# print "当前node 值:%s"%node.elem

	# 构建左子树
	if stringList[0] != "#":
		# print "构建node:%s的左子树"%node.elem
		node.lchild = Node()
		StringToTree(node.lchild,stringList)
	else:
		# print "node:%s没有左子树"%node.elem
		stringList.pop(0)

	# 构建右子树
	if stringList[0] != "#":
		# print "构建node:%s的右子树"%node.elem
		node.rchild = Node()		
		StringToTree(node.rchild,stringList)
	else:
		# print "node:%s没有右子树"%node.elem
		stringList.pop(0)

				

if __name__=="__main__":

	tree = Tree()
	elems = range(1,9)

	for elem in elems:
		tree.TreeAdd(elem)

	tree.TreeToStringRecur(tree.root)
	print tree.string
	print "++++++++++++++++++++++++++++"

	stringList = []
	newTree = Tree()
	stringList = tree.string.split('!')[:-1]
	StringToTree(newTree.root,stringList)
	newTree.TreeToStringRecur(newTree.root)
	print newTree.string