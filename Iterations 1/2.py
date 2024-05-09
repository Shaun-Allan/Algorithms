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

def shellSort(l):
    gap = len(l)//2
    start = time.time()
    while gap > 0:
        j = gap
        while j<len(l):
            i = j - gap
            while i>=0:
                if l[i+gap] > l[i]:
                    break
                else:
                    l[i+gap], l[i] = l[i], l[i+gap]
                i -=  gap
            j += 1
        gap //= 2
    end = time.time()
    runtime = end - start
    return l, runtime

def countingSort(l, base):
    output = [0] * len(l)
    count = [0] * 10

    for i in l:
        index = i//base
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i-1]

    for i in range(len(l)-1, -1, -1):
        index = l[i]//base
        output[count[index%10]-1] = l[i]
        count[index % 10] -= 1

    for i in range(len(l)):
        l[i] = output[i]
    

def radixExchangeSort(l):
    start = time.time()
    max_ = max(l)
    base = 1
    while max_/base >= 1:
        countingSort(l, base)
        base *= 10
    end = time.time()
    runtime = end - start
    return l, runtime

n = [10, 1000, 2000, 5000]
for i in n:
    l = generateList(i)
    print("\nInput Size: ", i)
    if i <= 100:
        print("List: ", l)
    print("\nInsertion Sort:")
    sortedInsertion, runtimeInsertion = insertionSort(l)
    if i <= 100:
        print("Sorted List: ", sortedInsertion)
    print("Runtime: ", runtimeInsertion)

    print("\nShell Sort:")
    sortedInsertion, runtimeInsertion = shellSort(l)
    if i<= 100:
        print("Sorted List: ", sortedInsertion)
    print("Runtime: ", runtimeInsertion)

    print("\nRadix Exchange Sort:")
    sortedInsertion, runtimeInsertion = radixExchangeSort(l)
    if i <= 100:
        print("Sorted List: ", sortedInsertion)
    print("Runtime: ", runtimeInsertion)

