def binary_search(arr, target):
    l = 0
    r = len(arr)
    while l < r:
        mid = (r + l) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

array = [1,2,2,3,4,5,6,10]
target = 11
res = binary_search(array, target)

print(f"{target} is {'not present' if res == -1 else 'present'} in {array} {'' if res == -1 else 'at index ' + str(res)}")