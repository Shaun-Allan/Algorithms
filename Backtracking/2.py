def isParanthesis(c):
    return c=="(" or c==")"

def isValidString(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count<0:
            return False
    return count==0

def minPara(str):
    if len(str) == 0:
        return
    
    visited = []
    q = []
    temp = ""
    level = False
    orgLen = len(str)
    q.append(str)
    visited.append(str)
    while len(q) > 0:
        str = q[0]
        q.pop(0)
        if isValidString(str):
            print(str)
            level = True
        if level:
            continue
        for i in range(len(str)):
            if not isParanthesis(str[i]):
                continue
            temp = str[:i] + str[i+1:]
            if temp not in visited:
                visited.append(temp)
                q.append(temp)
        
    return orgLen - len(str) - 1

expression = "()()))())"
print("String: ", expression)
min_count = minPara(expression)
print(f"Min Para to be removed: {min_count}")
print()
expression = "()v)"
print("String: ", expression)
min_count = minPara(expression)
print(f"Min Para to be removed: {min_count}")