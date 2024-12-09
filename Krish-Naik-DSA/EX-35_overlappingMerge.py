def merge_dicts_with_overlapping_keys(dicts):
    merge = {}
    for d in dicts:
        for key, value in d.items():
            if key in merge:
                merge[key] += value  
            else:
                merge[key] = value  
    return merge
