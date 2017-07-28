#!/usr/bin/python
# coding:utf-8
##
# Filename: QuickSort.py
# Author  : aiapple
# Date    : 2017-07-22
# Describe: 快速排序
#           
#           O(n*logN)
#
##
#############################################
import random

def QuickSort(List,left,right):
    if left > right:
        return -1

    # 随机找到一个基准数放在列表最后
    x = random.randint(0,right)
    List[x],List[right] = List[right],List[x]

    # q为一次划分完,随机值x的位置
    # 小于q位置的都比x 小,大于q位置的都比x大
    q = Partition(List,left,right)

    QuickSort(List,left,q-1)
    QuickSort(List,q+1,right)

    
def Partition(List,left,right):
    
    # 划分值x
    x = List[right]

    # mine 记录小于划分值的空间位置从-1开始
    # 即目前没有小于划分值的数
    mine = -1

    # j 用于遍历整个列表,找到小于等于空间
    for j in range(right):
        if List[j] <= x:
            mine = mine +1
            # 将小于划分值的数放入划分池
            List[mine],List[j]=List[j],List[mine]


    # 将划分值和小于等于空间之后的元素交换,完成划分过程
    List[mine+1],List[right]=List[right],List[mine+1]

    # 将划分值的位置返回
    return mine+1

if __name__=="__main__":

    L = [2,8,7,1,3,5,6,4,10,3,2,9]
    print "Input :",L
    QuickSort(L,0,len(L)-1)
    print "Output :",L
