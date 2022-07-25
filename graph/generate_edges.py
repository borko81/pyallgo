graph = {
    "a" : {"c"},
    "b" : {"c", "e"},
    "c" : {"a", "b", "d", "e"},
    "d" : {"c"},
    "e" : {"c", "b"},
    "f" : {}
}


def generate_edges(graph):
    edges = []
    isolated_node = set()
    for node in graph:
        # search node with not outgoing path
        if not graph[node]:
            isolated_node.add(node)
        for neighbour in graph[node]:
            edges.append({node: neighbour})
    return edges, isolated_node


print(generate_edges(graph))