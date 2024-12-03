def count_even_odd(lst):
    # Your code goes here
    e=0
    o=0
    for i in lst:
        if i%2==0:
            e+=1
        else:
            o+=1
    return e,o
print(count_even_odd( [1, 2, 3, 4, 5]))