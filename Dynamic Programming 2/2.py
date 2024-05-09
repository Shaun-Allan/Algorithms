def findLongestPalindrome(str_):
    if len(str_) <= 1:
        return str_
    max_len = 1
    dp = [[0 for j in range(len(str_))] for i in range(len(str_))]
    for i in range(len(str_)):
        dp[i][i] = 1
        for j in range(i):
            if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]==1):
                dp[j][i] = 1
                if i-j+1 > max_len:
                    max_len = i-j+1
    return max_len

s = input("Enter string: ")
print("The solution is " + str(findLongestPalindrome(s)))