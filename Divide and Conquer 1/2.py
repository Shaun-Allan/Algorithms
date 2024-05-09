def merge(l, r):
    i = 0
    j = 0
    inv_count = 0
    merged = []
    while i<len(l) and j<len(r):
        if l[i] <= r[j]:
            merged.append(l[i])
            i += 1
        else:
            inv_count += (len(l) - i)
            merged.append(r[j])
            j += 1
    while i<len(l):
        merged.append(l[i])
        i += 1
    while j<len(r):
        merged.append(r[j])
        j += 1
    return merged, inv_count

def merge_sort(arr):
    if len(arr) == 1:
        return arr, 0
    m = len(arr) // 2
    left, left_inv = merge_sort(arr[:m])
    right, right_inv = merge_sort(arr[m:])

    merged_arr, merge_inv = merge(left, right)

    total_inv = left_inv + right_inv + merge_inv
    return merged_arr, total_inv

l = [3,2,8,1]
sorted_l, inversions = merge_sort(l)
print("Sorted Array:", sorted_l)
print("Number of inversions:", inversions)
