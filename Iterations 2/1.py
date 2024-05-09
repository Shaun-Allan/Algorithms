def getUnique(l):
    unique = []
    for i in l:
        if l.count(i) == 1:
            unique.append(i)
    return unique

l = [3,6,9,2,3,9,1,15,21,3,1]
unique = getUnique(l)
print("Unique elements: ", unique)