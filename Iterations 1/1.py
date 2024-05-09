import random

def generateUnique(n):
    l = []
    while len(l) < n:
        num = random.randint(1,10000)
        if num not in l:
            l.append(num)
    return l

n = int(input("Enter n: "))
print(generateUnique(n))