#!/usr/bin/python
# coding:utf-8
##
# Filename: BinaryTree.py
# Author  : aiapple
# Date    : 2017-07-23
# Describe: 二叉树
#           树的构造
#            递归实现先序遍历、中序遍历、后序遍历
#            堆栈实现先序遍历、中序遍历、后序遍历
#            队列实现层次遍历
# 
#############################################
import pdb


class Node(object):
    """节点类"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""

    def __init__(self):
        # 初始化根节点
        self.root = Node()

    def add(self, elem):
        """
        	为树增加节点
        	按层次遍历,来增加
        """
        # print "Add elem"
        node = Node(elem)		  # 创建所需节点
        # print "new node value:%s"%node.elem
        if self.root.elem == -1:  # 如果根节点为空则直接赋值给根节点
            # print "root 为空"
            self.root = node
            # print "new root value:%s"%self.root.elem
        else:
            # 使用队列,对已有节点进行层次遍历
            myqueue = []
            myqueue.append(self.root)
            while myqueue:
                currentNode = myqueue.pop(0)         # 队列弹出当前节点
                # print "当前节点值:%s"%currentNode.elem
                if currentNode.lchild == None:       # 当节点没有左孩子,则将该节点赋值给当前左孩子
                    # print "%s 增加在左孩子上"%elem
                    currentNode.lchild = node
                    return
                elif currentNode.rchild == None:
                    # print "%s 增加在右孩子上"%elem
                    currentNode.rchild = node
                    return
                else:
                    # 当前节点有左右孩子,则分别将左右孩子,入队列
                    # print "当前节点值:%s 已经有左右孩子"%currentNode.elem
                    myqueue.append(currentNode.lchild)
                    myqueue.append(currentNode.rchild)  # 并继续查找,他们是否有左右孩子,并赋值

    def frontRecur(self, root):
        """
        	利用递归的方式实现先序遍历
        	并打印先序结果
        """
        if root is None:
        	return
        # 先根
        print root.elem
        # 再左
        self.frontRecur(root.lchild)
        # 后右
        self.frontRecur(root.rchild)

    def middleRecur(self, root):
        """
        	利用递归的方式实现中序遍历
        	并打印先序结果
        """
        if root is None:
        	return

        # 左
        self.middleRecur(root.lchild)
        # 根
        print root.elem
        # 右
        self.middleRecur(root.rchild)

    def laterRecur(self, root):
        """
        	利用递归的方式实现后序遍历
        	并打印先序结果
        """
        if root is None:
        	return
        # 左
        self.laterRecur(root.lchild)
        # 右
        self.laterRecur(root.rchild)
        # 根
        print root.elem

    def frontStack(self, root):
    	"""
    		利用非递归的方式实现先序遍历
    		0.将根节点压入stack中
    		1.从stack弹出顶节点,记为cur,打印cur值
    		2.如果右孩子不为空,将右孩子先入stack,如果左孩子不为空,左孩子再入stack
    		3.继续做1,2,直到stack为空
    	"""
    	myStack = []
    	myStack.append(root)
    	while myStack:
    		curNode = myStack.pop()
    		print curNode.elem
    		if curNode.rchild is not None:
    			myStack.append(curNode.rchild)  # 注意是右孩子先压入stack
    		if curNode.lchild is not None:
    			myStack.append(curNode.lchild)

    def middleStack(self, root):
    	"""
    		利用非递归的方式实现中序遍历
    		0.cur = root
    		1.将整个树的左边界压入stack,stack.append(cur),cur = cur.lchild 循环做
    		2.当cur == none 整个左边界全部入stack
    		  此时弹出node=stack.pop() 并打印node.elem cur=node.rchild
    		3.继续做1,2,直到 stack==null and cur = None 结束
    	"""
    	myStack = []
    	curNode = root

        # 注意不能先将root 压入stack 会两次将root节点压入
    	# myStack.append(curNode)

    	while myStack or curNode:
            while curNode:
                myStack.append(curNode)
                curNode = curNode.lchild  # 注意先将左边界全部压入stack
                
            node = myStack.pop()
            print node.elem
            curNode = node.rchild

    def laterStack(self, root):
    	"""
    		利用非递归的方式实现后序遍历
    		0.stack1.append(root)
    		1.从Stack1弹出cur,将cur的左孩子先入,再入右孩子
    		  cur=stack1.pop(),stack1.append(cur.lchild),stack1.append(cur.rchild)
    		2.每次从stack1弹出的cur 都放入stack2
    		3.不断重复1,2步骤,直到stack1为空,依次弹出stack2的节点便是后序结果
    	"""
    	myStack1 = []
    	myStack2 = []

    	myStack1.append(root)
    	#
    	while myStack1:
    		curNode = myStack1.pop()
    		myStack2.append(curNode)

    		if curNode.lchild is not None:
    			myStack1.append(curNode.lchild)
    		if curNode.rchild is not None:
    			myStack1.append(curNode.rchild)

    	while myStack2:
    		print myStack2.pop().elem

    def levelQueue(self, root):
    	"""
    		利用队列实现树的层次遍历
    	"""
    	myQueue = []
    	myQueue.append(root)

    	while myQueue:
            curNode = myQueue.pop(0)
            print curNode.elem
            # print "层次遍历 当前节点值:",curNode.elem
            if curNode.lchild is not None:
                # print "层次遍历 当前节点有左孩子:%s"%curNode.lchild.elem
                myQueue.append(curNode.lchild)
            if curNode.rchild is not None:
                # print "层次遍历 当前节点有右孩子:%s"%curNode.rchild.elem
                myQueue.append(curNode.rchild)


if __name__ == "__main__":
    # 生成树,并加入节点
    elems = range(1,9)
    tree = Tree()

    for elem in elems:
		tree.add(elem)
    
    # print '队列实现层次遍历:'
    # tree.levelQueue(tree.root)

    # print '递归实现先序遍历:'
    # tree.frontRecur(tree.root)
    # print '递归实现中序遍历:' 
    # tree.middleRecur(tree.root)
    # print '递归实现后序遍历:'
    # tree.laterRecur(tree.root)

    print '堆栈实现先序遍历:'
    tree.frontStack(tree.root)

    # print '堆栈实现中序遍历:'
    # tree.middleStack(tree.root)
    
    # print '堆栈实现后序遍历:'
    # tree.laterStack(tree.root)
