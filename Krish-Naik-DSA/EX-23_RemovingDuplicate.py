def remove_duplicates(lst):
    # Your code goes here
    items=[]
    for i in lst:
        if i not in items:
            items.append(i)
    return items
print(remove_duplicates( [1, 2, 3, 4, 5]))
# return list(set(lst)) easy way 