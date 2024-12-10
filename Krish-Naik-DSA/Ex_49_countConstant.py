def count_consonants(s):
    """
    Function to count the number of consonants in the input string.
    
    Parameters:
    s (str): The input string to check for consonants.
    
    Returns:
    int: The count of consonants in the input string.
    """
    # Your code here
    s = s.replace(' ', '')  
    s = s.lower() 
    vowels = 'aeiou'  
    count = 0
    
    for char in s:
        if char.isalpha() and char not in vowels:  
            count += 1
            
    return count