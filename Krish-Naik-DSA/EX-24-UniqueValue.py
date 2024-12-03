def check_unique(lst):
    # Your code goes here
    if len(set(lst)) == len(lst):
        return True
    else:
        return False