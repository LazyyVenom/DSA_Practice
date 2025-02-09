def sum_back(prev_sum, num):
    if num == 0:
        return prev_sum
    return sum_back(prev_sum + num, num - 1)

# print(sum_back(0,100))

# print(100 * (100 + 1) // 2)

def fac(res ,num):
    if num == 0 or num == 1:
        return res
    return fac(res * num, num - 1)

print(fac(1, 6))