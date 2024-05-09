def maxCrossingSum(arr, low, mid, high):
    sm = 0
    left_sum = float('-inf')
    for i in range(mid, low-1, -1):
        sm += arr[i]
        if sm > left_sum:
            left_sum = sm

    sm = 0
    right_sum = 0
    for i in range(mid, high+1):
        sm += arr[i]
        if sm > right_sum:
            right_sum = sm

    return max(left_sum + right_sum - arr[mid], left_sum, right_sum)

def maxSubarraySum(arr, low, high):
    if low>high:
        return -1 #invalid case
    if low==high:
        return arr[low]
    mid = (low+high)//2

    return max(maxSubarraySum(arr, low, mid-1), maxSubarraySum(arr, mid+1, high), maxCrossingSum(arr, low, mid, high))


arr = [-2,1,-3,4,-1,2,1,-5,4] 
n = len(arr) 
  
max_sum = maxSubarraySum(arr, 0, n-1) 
print("Maximum contiguous sum is ", max_sum) 