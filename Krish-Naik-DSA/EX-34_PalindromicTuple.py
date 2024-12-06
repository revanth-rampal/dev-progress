def is_palindromic_tuple(tup):
    # Your code goes here
    a=tup[::-1]
    if tup == a:
        return True
    else:
        return False
print(is_palindromic_tuple((1, 2, 3, 2, 1)))