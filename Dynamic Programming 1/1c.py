dp = {}
vs = {}

def LCSTD(s1, s2):
    if len(s1)==0 or len(s2)==0:
        return ""
    dp_i = (s1, s2)
    if dp_i in vs:
        return dp[dp_i]
    else:
        vs[dp_i] = 1
    
    if s1[-1] == s2[-1]:
        res = s1[-1] + LCSTD(s1[:-1], s2[:-1])
        dp[dp_i] = res
        return res
    
    sub1 = LCSTD(s1[:-1], s2)
    sub2 = LCSTD(s1, s2[:-1])
    res = sub1 if len(sub1)>len(sub2) else sub2
    dp[dp_i] = res
    return res

def LCS(s1, s2):
    return LCSTD(s1, s2)[::-1]

s1 = input("Enter s1: ")
s2 = input("Enter s2: ")
print("LCS: ", LCS(s1, s2))