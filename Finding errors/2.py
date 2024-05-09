def comparison_count_sort(nums):
    count = [0] * (max(nums)+1)
    nums_sorted = [0] * len(nums)
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                count[nums[i]] += 1
            elif nums[i] < nums[j]:
                count[nums[j]] += 1
    for i in nums:
        nums_sorted[count[i]] = i
    return nums_sorted

l = [75,5,3,6,4,9,1,8]
print("List: ", l)
print("Sorted List: ", comparison_count_sort(l))
