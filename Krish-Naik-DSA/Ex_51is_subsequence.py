def is_subsequence(s, t):
    """
    Function to check if t is a subsequence of s.
    
    Parameters:
    s (str): The original string.
    t (str): The target subsequence string.
    
    Returns:
    bool: True if t is a subsequence of s, False otherwise.
    """
    # Your code here
    
    i,j=0,0
    while i<len(s) and j<len(t):
        if s[i]==t[j]:
             j+=1
        i+=1
    return j == len(t)
        
            
    
