def ffloydWarshall(adj, v1, v2):
    adj = [[float('inf') if adj[i][j]==0 and not i==j else adj[i][j] for j in range(len(adj))] for i in range(len(adj))]
    for k in range(len(adj)):
        for i in range(len(adj)):
            for j in range(len(adj)):
                adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])
    return adj[v1][v2]

adj = [ [ 0, 4, 0, 0, 0, 0, 0, 8, 0 ],      
        [ 4, 0, 8, 0, 0, 0, 0, 11, 0 ],
        [ 0, 8, 0, 7, 0, 4, 0, 0, 2 ],
        [ 0, 0, 7, 0, 9, 14, 0, 0, 0 ],
        [ 0, 0, 0, 9, 0, 10, 0, 0, 0 ],
        [ 0, 0, 4, 14, 10, 0, 2, 0, 0 ],
        [ 0, 0, 0, 0, 0, 2, 0, 1, 6 ],
        [ 8, 11, 0, 0, 0, 0, 1, 0, 7 ],
        [ 0, 0, 2, 0, 0, 0, 6, 7, 0 ] ]

print("ADJACENCY MATRIX\n")
print(*adj, sep="\n")
print()
v1 = int(input("Enter v1: "))
v2 = int(input("Enter v2: "))
print(f"Minimum Distance between {v1} and {v2}: " + str(ffloydWarshall(adj, v1, v2)))
    