graph = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def get_vertices(self):
        return list(self.gdict.keys())

    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

    def add_vertex(self, key: str):
        if key not in self.gdict:
            self.gdict[key] = []

    def add_edge(self, edge):
        edge = list(set(edge))
        key, value, *_ = edge
        if key in self.gdict:
            self.gdict[key].append(value)
        else:
            self.gdict[key] = [value]


g = Graph(graph)
print(g.get_vertices())
print(g.findedges())
g.add_vertex('f')
print(g.get_vertices())
g.add_edge({'a', 'e'})
print(g.findedges())
