def merge_lists_to_dictionary(keys, values):
    # Your code goes here
    if len(keys) != len(values):
        return False
    else:
        return dict(zip(keys, values))

print(merge_lists_to_dictionary(['a', 'b', 'c'],[1, 2, 3]))
        
