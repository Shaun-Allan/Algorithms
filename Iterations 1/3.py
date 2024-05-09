import random
import time

def generateList(n):
    l = []
    for i in range(n):
        num = random.randint(1,10000)
        l.append(num)
    return l

def insertionSort(l):
    start = time.time()
    for i in range(len(l)):
        key = l[i]
        j = i-1
        while j>=0 and key<l[j]:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    end = time.time()
    runtime = end - start
    return l,runtime

l = generateList(10000)
sorted_l = sorted(l)
sorted_l_rev = sorted(l, reverse=True)

print("Runtime Performance")
ascList, ascRuntime = insertionSort(sorted_l)
print("Sorted in ascending order: ", ascRuntime)
descList, descRuntime = insertionSort(sorted_l_rev)
print("Sorted in descending order: ", descRuntime)
notSortList, notSortRuntime = insertionSort(l)
print("Not Sorted: ", notSortRuntime)