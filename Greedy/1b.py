def printSolution(edges, parent, src):
    print("Edge\tWeight")
    for i in range(len(edges)):
        if i != src:
            print(f"{parent[i]}--{i}\t{edges[i]}")

def minEdge(edges, visited):
    min_ = float('inf')
    min_index = 0
    for v in range(len(edges)):
        if edges[v]<min_ and not visited[v]:
            min_ = edges[v]
            min_index = v
    return min_index

def prims(adj, src):
    edges = [float('inf')] * len(adj)
    parent = [None] * len(adj)
    edges[src] = 0
    visited = [False] * len(adj)
    parent[src] = -1

    for count in range(len(adj)):
        u = minEdge(edges, visited)
        visited[u] = True
        for v in range(len(adj)):
            if adj[u][v]>0 and not visited[v] and edges[v]>adj[u][v]:
                edges[v] = adj[u][v]
                parent[v] = u
    printSolution(edges, parent, src)


adj = [[0, 3, 0, 0, 6, 5],
       [3, 0, 1, 0, 0, 4],
       [0, 1, 0, 6, 0, 4],
       [0, 0, 6, 0, 8, 5],
       [6, 0, 0, 8, 0, 2],
       [5, 4, 4, 5, 2, 0]]
prims(adj, 0)