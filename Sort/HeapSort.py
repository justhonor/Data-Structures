#!/usr/bin/python
# coding:utf-8
##
# Filename: HeapSort.py
# Author  : aiapple
# Date    : 2017-07-28
# Describe: 堆排序
##
#############################################
#coding: utf-8 
#!/usr/bin/python   
import random
import math

#随机生成0~100之间的数值
def get_andomNumber(num):  
    lists=[]  
    i=0  
    while i<num:  
        lists.append(random.randint(0,100))  
        i+=1
    return lists


# 调整堆
def adjust_heap(lists, NodeI, size):
    """
        NodeI:   节点的序号
        lchild:  该节点左孩子的序号
        rchild:  该节点右孩子的序号
        size:    列表长度
    """
    lchild = 2 * NodeI + 1    # 列表序号从0开始,根节点list[0] ,其左孩子list[1] 
    rchild = 2 * NodeI + 2    # 右孩子 list[2]
    max = NodeI
    if NodeI < size / 2:      # 该节点不是叶子节点
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != NodeI:
            # 将字节点中最大的给根节点
            lists[max], lists[NodeI] = lists[NodeI], lists[max]
            # 避免调整之后以max为父节点的子树不是堆 
            adjust_heap(lists, max, size)

# 创建堆
def build_heap(lists, size):
    """
        堆的建立,从非叶节点,开始一层层向根,才能选出最大值放在根处
        列表存放,按层次遍历的二叉树;
        list[0] 为根 其左子数:list[1] 右子数:list[2]
    """
    for i in range(0, (int(size/2)))[::-1]:   #非叶节点最大序号为size/2
        adjust_heap(lists, i, size)

# 堆排序
def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)

    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        # 调整之后,只需对前n-1个节点 继续调整大根堆
        adjust_heap(lists, 0, i)
    return lists
 
if __name__ == '__main__':
    
    a = get_andomNumber(10)
    print("排序之前：%s" % a)

    b = heap_sort(a)
    print("排序之后：%s" % b)
