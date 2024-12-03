def find_largest(numbers):
    # Your code goes here
    # without using max function
    num=float("-inf")
    for i in numbers:
        if i>num:
            num=i
    return num
print(find_largest( [1, 2, 3, 4, 5]))