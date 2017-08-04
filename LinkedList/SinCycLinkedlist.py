#!/usr/bin/python
# coding:utf-8
##
# Filename: SinCycLinkedlist.py
# Author  : aiapple
# Date    : 2017-08-01
# Describe:
##
#############################################
import sys

class Node(object):
    """节点"""
    def __init__(self, item):
        self.item = item
        self.next = None

class SinCycLinkedlist(object):
    """单向循环链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def getHeadValue(self):
        """获取节点值"""
        return self._head.item

    def length(self):
        """返回链表的长度"""
        # 如果链表为空，返回长度0
        if self.is_empty():
            return 0
        count = 1
        cur = self._head
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self._head
        print cur.item,
        while cur.next != self._head:
            cur = cur.next
            print cur.item,
        print ""


    def add(self, item):
        """头部添加节点"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            #添加的节点指向_head
            node.next = self._head
            # 移到链表尾部，将尾部节点的next指向node
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            #_head指向添加node的
            self._head = node

    def append(self, item):
        """尾部添加节点"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            # 移到链表尾部
            cur = self._head
            # print "dang qian head:%s"%cur.item
            while cur.next != self._head:
                cur = cur.next
            # 将尾节点指向node
            cur.next = node
            # 将node指向头节点_head
            node.next = self._head

    def insert(self, pos, item):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def SortInsert(self,value):
        """有序链表中,插入某值依然有序"""
        node = Node(value)

        if self.is_empty():
            # 原链表为空
            self._head = node
            self._head.next = self._head
        else:
            # 原链表不为空
            print "head==%s"%self._head.item
            pre = self._head
            cur = self._head.next
            while cur.next != self._head:
                if value <= cur.item and value >= pre.item:
                    pre.next = node
                    node.next = cur
                    print "插入:%s"%value
                    return self._head
                else:
                    pre = cur
                    cur = cur.next

            # cur在最后的位置,插入位置在head之前
            # 两种情况:
            #            插入值比头节点小,插入值比尾节点大
            if value >= cur.item:
                cur.next = node
                node.next = self._head
                return self._head
            else:
                cur.next = node
                node.next = self._head
                self._head = node
                return self._head

    def remove(self, item):
        """删除一个节点"""
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        # 将cur指向头节点
        cur = self._head
        pre = None
        # 若头节点的元素就是要查找的元素item
        if cur.item == item:
              # 如果链表不止一个节点
            if cur.next != self._head:
                # 先找到尾节点，将尾节点的next指向第二个节点
                while cur.next != self._head:
                    cur = cur.next
                # cur指向了尾节点
                cur.next = self._head.next
                self._head = self._head.next
            else:
                # 链表只有一个节点
                self._head = None
        else:
            pre = self._head
            # 第一个节点不是要删除的
            while cur.next != self._head:
                # 找到了要删除的元素
                if cur.item == item:
                    # 删除
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            # cur 指向尾节点
            if cur.item == item:
                # 尾部删除
                pre.next = cur.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self._head
        if cur.item == item:
            return True
        while cur.next != self._head:
            cur = cur.next
            if cur.item == item:
                return True
        return False

if __name__ == "__main__":
    a = [3,7,7,8,12,13,13]
    insert = [2,3,4,7,8,9,13,14]
    
    ll = SinCycLinkedlist()
    for aa in a:
        ll.append(aa)
        # print "head is :%s"%(ll.getHeadValue())

    for i in insert:
        print "%s  insert:%s"%(a,i)
        ll.SortInsert(i)
        ll.travel()