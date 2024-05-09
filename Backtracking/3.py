def is_safe(vertex, color, adj_matrix, color_assignment, k):
    for v in range(len(adj_matrix)):
        if adj_matrix[vertex][v] == 1 and color_assignment[v] == color:
            return False
    return True

def color_graph_util(vertex, adj_matrix, k, color_assignment):
    if vertex == len(adj_matrix):
        return True
    
    for color in range(1, k+1):
        if is_safe(vertex, color, adj_matrix, color_assignment, k):
            color_assignment[vertex] = color
            if color_graph_util(vertex+1, adj_matrix, k, color_assignment):
                return True
            color_assignment[vertex] = 0
    
    return False

def color_graph(adj_matrix, k):
    color_assignment = [0] * len(adj_matrix)
    
    if not color_graph_util(0, adj_matrix, k, color_assignment):
        print("No solution exists.")
        return
    
    print("Color assignments:")
    for vertex, color in enumerate(color_assignment):
        print(f"Vertex {vertex}: Color {color}")

# Sample Input
V = 4
E = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
k = 3

# Initialize adjacency matrix
adj_matrix = [[0] * V for _ in range(V)]
for u, v in E:
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1

print("Adjacency Matrix:")
print(*adj_matrix, sep="\n")
print("K: ", k)
print()

# Color the graph
color_graph(adj_matrix, k)
