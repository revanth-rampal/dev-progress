
def rotate_list(lst, k):
    # Handle empty list
    if not lst:
        return lst
    
    n = len(lst)
    k = k % n  # Normalize k
    if k == 0:  # No rotation needed if k is 0
        return lst

    # Create a new list for the rotated result
    rotated = [0] * n
    for i in range(n):
        rotated[(i + k) % n] = lst[i]

    return rotated


