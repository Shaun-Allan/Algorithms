def findMax(arr):
    if(len(arr) == 1):
        return arr[0]
    m = len(arr)//2
    l = findMax(arr[0:m])
    r = findMax(arr[m:len(arr)])
    if l>=r:
        return l
    else:
        return r
    
l = [1,5,3,7,8,98,23,65,34]
print("List: ", l)
print("Max: ", findMax(l))