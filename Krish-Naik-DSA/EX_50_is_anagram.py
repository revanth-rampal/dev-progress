def is_anagram(s, t):
    """
    Function to check if t is an anagram of s.
    
    Parameters:
    s (str): The first input string.
    t (str): The second input string.
    
    Returns:
    bool: True if t is an anagram of s, False otherwise.
    """
    # Your code here
    if sorted(s) != sorted(t):
        return False
    else:
        return True 

 