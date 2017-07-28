#!/usr/bin/python
# coding:utf-8
##
# Filename: Merge.py
# Author  : aiapple
# Date    : 2017-07-22
# Describe: 归并排序
#           1. 使用二分法将列表分成n个小列表
##          2. 对领二分树的左右两子数,进行有序列表的合并
########################################################

# 将两个有序列表合成成一个有序列表
def Merge(leftList,rightList):
    merged = []

    left=right=0

    # 依次比较两个列表值,一直某个列表遍历完成
    while left<len(leftList) and right<len(rightList):
        if leftList[left] < rightList[right]:
            merged.append(leftList[left])
            left = left + 1
        else:
            merged.append(rightList[left])
            right = right + 1

    # 当某个列表遍历完成,将另一个列表剩余元素添加到合并列表中
    if left==len(leftList):
        for i in rightList[right:]:
            merged.append(i)
    else:
        for i in leftList[left:]:
            merged.append(i)

    return merged

def MergeSort(List):
    if len(List) <=1:
        return List

    # 用递归二分法将列表分成长度为1的列表
    middle = len(List)/2

    leftList = MergeSort(List[:middle])
    rightList = MergeSort(List[middle:])

    return Merge(leftList,rightList)
    

if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    print "Input:",a
    print "Output:",MergeSort(a)
