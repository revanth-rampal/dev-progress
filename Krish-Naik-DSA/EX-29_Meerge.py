def merge_two_sorted_lists(list1, list2):
    # Your code goes here
    a=list1+list2
    b= list(set(a))
    return b 
print(merge_two_sorted_lists([1, 4, 7],[2, 3, 5, 8]))