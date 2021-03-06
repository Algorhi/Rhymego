#!/usr/bin/env python3

class Node(object):
    def __init__(self,item):
        self.item = item #表示对应的元素
        self.left = None #表示左子节点
        self.right = None #表示右子节点

    def __str__(self):
        # print 一个Node类时会打印 __str__ 的返回值
        return str(self.item)

class Tree(object):
    def __init__(self):
        # 根节点定义为root永不删除，作为哨兵使用
        self.root = Node('root')

    def add(self,item):
        node = Node(item)
        #
        if self.root is None:
            self.root = node
        else:
            #
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                # 
                if pop_node.left is None:
                    pop_node.left is node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def get_parent(self,item):
        if self.root.item == item:
            #
            return None
        # 
        tmp = [self.root]
        while tmp:
            pop_node = tmp.pop(0)
            #
            if pop_node.left and pop_node.left.item == item:
                # 
                return pop_node
            #
            if pop_node.right and pop_node.right.item == item:
                # 
                return pop_node
            #
            if pop_node.left is not None:
                tmp.append(pop_node.left)
            if pop_node.right is not None:
                tmp.append(pop_node.right)
        return

    def delete(self,item):
        #
        if self.root is None:
            return False

        parent = self.get_parent(item)
        if parent:
            # 
            del_node = parent.left if parent.left.item == item else parent.right
            #
            if del_node.left is None:
                #
                if parent.left.item == item:
                    parent.left = del_node.right
                #
                else:
                    parent.right = del_node.right
                # 
                del del_node
                return True
            #
            elif del_node.right is None:
                # 
                if parent.left.item == item:
                    parent.left = del_node.left
                #
                else:
                    parent.right = del_node.left
                # 
                del del_node
                return True
            #
            else:
                tmp_pre = del_node
                #
                tmp_next = del_node.right
                #
                if tmp_next.left is None:
                    #
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                else:
                    #
                    while tmp_next.left:
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    #
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                #
                if parent.left.item == item:
                    parent.left = tmp_next
                #
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            return False

