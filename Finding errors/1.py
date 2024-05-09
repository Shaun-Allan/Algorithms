def count_inversions(nums):
    count = 0
    inversion = []
    for i in range(1, len(nums)):
        j = i-1
        while j>=0:
            if nums[i] < nums[j]:
                inversion.append((nums[j], nums[i]))
                count += 1
            j -= 1
    return count, inversion

l = [3,2,8,1]
count, inversion = count_inversions(l)
print("Number of Inversions: ", count)
print("Inversions: ", inversion)
