import random
import time


def generateList(n):
    l = []
    for i in range(n):
        num = random.randint(1,10000)
        l.append(num)
    return l


def binarySearch(arr, key):
    l = 0
    r = len(arr) - 1
    start = time.time()
    while l<=r:
        m = (l+r)//2
        if key < arr[m]:
            r = m-1
        elif key > arr[m]:
            l = m+1
        else:
            runtime = time.time() - start
            return m, runtime
        
def binarySearchRecursive(arr, key, l, r, runtime):
    m = (l+r)//2
    start = time.time()
    if key < arr[m]:
        return binarySearchRecursive(arr, key, l, m-1, runtime+time.time()-start)
    elif key > arr[m]:
        return binarySearchRecursive(arr, key, m+1, r, runtime+time.time()-start)
    else:
        return m, runtime

l = generateList(100000) 
l.sort()
key = random.choice(l)

print("Performnce Comparison")
nonRecIndex, nonRecRuntime = binarySearch(l, key)
print("\nNon-Recursive Binary Search Result: ", nonRecIndex)
print("Non-Recursive Binary Search Runtime: ", nonRecRuntime)
recIndex, recRuntime = binarySearchRecursive(l, key, 0, len(l)-1, 0)
print("\nRecursive Binary Search Result: ", recIndex)
print("Recursive Binary Search Runtime: ", recRuntime)

