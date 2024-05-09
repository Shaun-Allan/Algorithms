def minDistance(dist, visited):
    min_ = float('inf')
    min_index = 0
    for u in range(len(dist)):
        if dist[u]<min_ and not visited[u]:
            min_ = dist[u]
            min_index = u
    return min_index

def dijkstra(adj, src):
    dist = [float('inf')] * len(adj)
    dist[src] = 0
    visited = [False] * len(adj)
    for count in range(len(adj)):
        u = minDistance(dist, visited)
        visited[u] = True
        for v in range(len(adj)):
            if adj[u][v]>0 and not visited[v] and dist[v]>dist[u]+adj[u][v]:
                dist[v] = dist[u] + adj[u][v]
    return dist

def printSolution(src, dist):
    print(f"Source: {src}")
    print("Target\tDistance")
    for i in range(len(dist)):
        print(f"{i}\t{dist[i]}")


adj = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
       [4, 0, 8, 0, 0, 0, 0, 11, 0],
       [0, 8, 0, 7, 0, 4, 0, 0, 2],
       [0, 0, 7, 0, 9, 14, 0, 0, 0],
       [0, 0, 0, 9, 0, 10, 0, 0, 0],
       [0, 0, 4, 14, 10, 0, 2, 0, 0],
       [0, 0, 0, 0, 0, 2, 0, 1, 6],
       [8, 11, 0, 0, 0, 0, 1, 0, 7],
       [0, 0, 2, 0, 0, 0, 6, 7, 0]]
dist = dijkstra(adj, 0)
printSolution(0, dist)
