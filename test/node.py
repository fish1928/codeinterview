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
    # [0] test for initialize_nodes and to string
    head = initialize_nodes(20)
    print(head)

