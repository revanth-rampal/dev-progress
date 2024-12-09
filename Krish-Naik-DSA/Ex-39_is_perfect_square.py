def is_perfect_square(num):
    """
    Function to check if a number is a perfect square.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    bool: True if num is a perfect square, False otherwise.
    """
    # Your code here
    if num<0:
        return False
    for i in range(int(num**0.5)+1):
        if i**2==num:
            return True
    return False
print(is_perfect_square(6))
