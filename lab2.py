class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kraskal(vertices, edges):
    edges.sort(key=lambda x: x[2])
    disjoint_set = DisjointSet(vertices)
    mst = []

    for u, v, weight in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append((u, v, weight))

    return mst


def visualize_graph(edges, filename='graph.dot'):
    dot_graph = 'graph G {\n' + ''.join(f'    {u} -- {v} [label="{weight}"];\n' for u, v, weight in edges) + '}'

    with open(filename, 'w') as f:
        f.write(dot_graph)


if __name__ == "__main__":
    #edges = [
    #    (0, 1, 4),
    #    (0, 2, 1),
    #    (1, 2, 2),
    #    (1, 3, 5),
    #    (2, 3, 8),
    #    (3, 4, 6),
    #    (1, 4, 3)
    #]
    edges = [
        (0, 1, 7),
        (0, 2, 6),
        (0, 3, 8),
        (1, 2, 8),
        (1, 4, 5),
        (2, 3, 5),
        (3, 4, 9),
        (2, 4, 7)
    ]

    vertices = 6
    mst = kraskal(vertices, edges)

    print("Минимальное остовное дерево:")
    for u, v, weight in mst:
        print(f"{u} -- {v} (вес: {weight})")

    visualize_graph(edges, 'input_graph.dot')
    visualize_graph(mst, 'mst_graph.dot')
