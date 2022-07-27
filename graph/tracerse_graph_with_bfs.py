class Node:

    def __init__(self, name):
        self.name = name
        self.node_list = []
        self.visited = False


def breath_first_search(start):
    queue = [start]

    while queue:
        actual_node = queue.pop(0)
        print(actual_node.name)
        actual_node.visited = True

        for n in actual_node.node_list:
            if not n.visited:
                queue.append(n)


if __name__ == '__main__':
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')

    node1.node_list.append(node2)
    node1.node_list.append(node3)
    node2.node_list.append(node4)

    breath_first_search(node1)
