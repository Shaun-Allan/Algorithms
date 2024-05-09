def domino_solitaire(grid):
    n = len(grid[0])  
    dp = [0] * (n + 1)  
    
    dp[0] = 0
    dp[1] = abs(grid[0][0] - grid[1][0])
    
    for i in range(2, n + 1):
        score_h = abs(grid[0][i-1] - grid[1][i-1]) + dp[i-1]
        score_v = abs(grid[0][i-2] - grid[0][i-1]) + abs(grid[1][i-2] - grid[1][i-1]) + dp[i-2]
        dp[i] = max(score_h, score_v)
    
    return dp[n]

grid = [
    [8,6,2,3],
    [9,7,1,2]
]

print("Grid:")
print(*grid, sep="\n")
print("Maximum score:", domino_solitaire(grid))
