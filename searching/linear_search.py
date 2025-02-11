def linear_search(arr, target):
    for idx, ele in enumerate(arr):
        if ele == target:
            return idx
    return -1

array = [1,2,4,5,6,3,10,2]
target = 10
res = linear_search(array, target)

print(f"{target} is {'not present' if res == -1 else 'present'} in {array} {'' if res == -1 else 'at index ' + str(res)}")