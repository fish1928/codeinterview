# 定义单链表：一组Nodes对象，其中每一个Node对象next指向下一个，没有循环
# index 只是用来方便打印链表操作，暂定是从1开始的int
class Node:
    def __init__(self, index):
        self.index = index
        self.next = None
    # end

    def __str__(self):
        pass
# end Node

# n 从1开始
def remove_node_n(head, n):
    pass



# return 指定数量Node的单链表，返回头节点，不考虑特殊情况
def initialize_nodes(quantity):
    return None


if __name__ == "__main__":
    # 单链表创建 example
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    n1.next = n2
    n2.next = n3
    # 以上代码完成节点数为3的单链表
    # 其中该单链表由n1,n2,n3组成
    # 其中 n1是头节点


    # [0] test for initialize_nodes and to string
    head = initialize_nodes(20)
    print(head)

