class UnionFind:
    def __init__(self):
        self.components = {}
        self.size = 0
    def initialize(self, vertices):
        self.size = vertices
        for v in range(vertices):
            self.components[v] = v
    def find(self, vertex):
        return self.components[vertex]
    def union(self, u, v):
        c_old = self.components[u]
        c_new = self.components[v]
        for k in range(self.size):
            if self.components[k] == c_old:
                self.components[k] = c_new

def minEdge(adj, visited):
    min_ = float('inf')
    min_edge = (0,0)
    for i in range(len(adj)):
        for j in range(i+1, len(adj)):
            if adj[i][j]<min_ and not visited[i][j] and adj[i][j]!=0:
                min_ = adj[i][j]
                min_edge = (i, j)
    return min_edge


def kruskals(adj):
    unionfind = UnionFind()
    unionfind.initialize(len(adj))
    visited = [[False for i in range(len(adj))] for j in range(len(adj))]
    mst = []

    for count in range((len(adj)*(len(adj)-1))//2):
        (u, v) = minEdge(adj, visited)
        visited[u][v] = True
        if unionfind.find(u) != unionfind.find(v):
            unionfind.union(u, v)
            mst.append((u, v))
    return mst

def printSolution(edges, adj):
    print("Edge\tWeight")
    for i in edges:
        print(f"{i[0]}--{i[1]}\t{adj[i[0]][i[1]]}")

adj = [[0, 3, 0, 0, 6, 5],
       [3, 0, 1, 0, 0, 4],
       [0, 1, 0, 6, 0, 4],
       [0, 0, 6, 0, 8, 5],
       [6, 0, 0, 8, 0, 2],
       [5, 4, 4, 5, 2, 0]]

mst = kruskals(adj)
printSolution(mst, adj)
            

    


    




adj = [[0, 3, 0, 0, 6, 5],
       [3, 0, 1, 0, 0, 4],
       [0, 1, 0, 6, 0, 4],
       [0, 0, 6, 0, 8, 5],
       [6, 0, 0, 8, 0, 2],
       [5, 4, 4, 5, 2, 0]]