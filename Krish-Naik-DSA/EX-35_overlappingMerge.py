
def merge_dicts_with_overlapping_keys(dicts):
    # Your code goes here
    merge={}
    words = dicts.split()
    for i in words:
        if i in merge:
            merge[i]=words[i]+merge[i]
        else:
             merge[i]=words[i]
    return merge


            