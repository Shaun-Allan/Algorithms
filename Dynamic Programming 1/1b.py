def LCSDP(s1, s2):
    L = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i==0 or j==0:
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    lcs = ""
    i = len(s1)
    j = len(s2)
    while i>0 and j>0:
        if s1[i-1] == s2[j-1]:
            lcs += s1[i-1]
            i -= 1
            j -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    lcs = lcs[::-1]
    return lcs

s1 = input("Enter s1: ")
s2 = input("Enter s2: ")
print("LCS: ", LCSDP(s1, s2))