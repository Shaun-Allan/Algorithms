def LCSRec(s1, s2):
    if len(s1)==0 or len(s2)==0:
        return ""
    elif s1[-1] == s2[-1]:
        return LCSRec(s1[:-1], s2[:-1]) + s1[-1]
    else:
        sub1 = LCSRec(s1[:-1], s2)
        sub2 = LCSRec(s1, s2[:-1])
        return sub1 if len(sub1)>len(sub2) else sub2

s1 = input("Enter s1: ")
s2 = input("Enter s2: ")
print("LCS: ", LCSRec(s1, s2))