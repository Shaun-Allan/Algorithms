def findKInsertion(arr, k):
    if k<1 or k>len(arr):
        return "Invalid k"
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr[k-1]

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    while left <= right:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right

def findKQuick(arr, k, low, high):
    if k<1 or k>len(arr):
        return "Invalid k"
    if low < high:
        pivotIndex = partition(arr, low, high)
        findKQuick(arr, k, low, pivotIndex-1)
        findKQuick(arr, k-pivotIndex+low, pivotIndex+1, high)
        return arr[k-1]
        


l = [4,6,4,3,7,8,6,7,3,4,1]
print("List: ", l)
k = int(input("Enter k: "))
print(f"{k}th smallest element using Insertion Sort: {findKInsertion(l, k)}")
print(f"{k}th smallest element using Quick Sort: {findKQuick(l, k, 0, len(l)-1)}")