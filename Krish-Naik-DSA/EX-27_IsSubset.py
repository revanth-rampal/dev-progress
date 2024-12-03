def is_subset(lst1, lst2):
    # Your code goes here
   return all(i in lst2 for i in lst1)
