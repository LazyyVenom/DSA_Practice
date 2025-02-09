def sum_back(prev_sum, num):
    if num == 0:
        return prev_sum
    return sum_back(prev_sum + num, num - 1)

print(sum_back(0,100))

print(100 * (100 + 1) // 2)