def max_consecutive_difference(lst):
    if len(lst) < 2:
        return 0
    max_diff = 0
    for i in range(len(lst) - 1):
        diff = abs(lst[i] - lst[i + 1])
        if diff > max_diff:
            max_diff = diff
    return max_diff

print(max_consecutive_difference([1, 7, 3, 10]))
