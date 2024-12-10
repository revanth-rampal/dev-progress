def is_palindrome(s):
    """
    Function to check if the input string is a palindrome.
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Your code here
    s=s.replace(" ","")
    s=s.lower()
    if s[::-1]==s:
        return True 
    else:
        return False