def subsetSum(i, _set, target_sum, subset):
    if target_sum == 0:
        print(subset, end=", ")
        return
    if i==len(_set):
        return 
    subsetSum(i+1, _set, target_sum, subset)
    if _set[i] <= target_sum:
        subset.append(_set[i])
        subsetSum(i+1, _set, target_sum-_set[i], subset)
        subset.pop()

l = [2,3,5,6,8,10]
print("List: ", l)
sum = int(input("Enter sum: "))
subsetSum(0, l, 10, [])