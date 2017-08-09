#!/usr/bin/python
# coding:utf-8
##
# Filename: findPath_25.py
# Author  : aiapple
# Date    : 2017-08-9
# Describe: 剑指offter NO.25
#           
#		输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
#   路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
##
#############################################
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
			# print "当前节点值:%s"%cur.elem
			if cur.lchild is None:
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
			cur = myqueue.pop(0	)
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
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.path = []
        self.curNumber = 0
        self.rpath = []
    
    def findPath(self, root, expectNumber):
        # write code here
        if not root:
            return False
        
        self.path.append(root)
        self.curNumber += root.elem
        
        print "curnode val:%s curnumber:%s"%(root.elem,self.curNumber)
        # 如果是页节点
        if  not root.lchild and not root.rchild:
        	print "%s是 叶子节点 curnumber=%s "%(root.elem,self.curNumber)
        	if self.curNumber == expectNumber:
        		pp = []
        		for p in self.path:
        			pp.append(p.elem)
        		self.rpath.append(pp)
            	print "path add rpath:%s"%self.rpath
        
        # 如果不是页节点则遍历它的子节点
        if root.lchild:
            self.FindPath(root.lchild,expectNumber)
            
        if root.rchild:
            self.FindPath(root.rchild,expectNumber)
            
        # 返回父节点的时候将当前节点从path中删除
        node=self.path.pop()
        self.curNumber -= node.elem
        
        
    def FindPath(self,root, expectNumber):
        # write code here
        self.findPath(root,expectNumber)
        return self.rpath

if __name__ == '__main__':

	tree = Tree()
	elems =[8,4,2,1,5,7,3]
	for elem in elems:
		tree.treeAdd(elem)
	tree.treePrinter(tree.root)

	s = Solution()
	print s.FindPath(tree.root,17)

d = {}
d.items








		
