def sum_of_even_numbers(n):
    """
    Function to return the sum of the first n even natural numbers.
    
    Parameters:
    n (int): The number of even numbers to sum.
    
    Returns:
    int: The sum of the first n even natural numbers.
    """
    # Your code here
    even=0
    for i in range(1,n+1):
         even=even +(2*i)
    return even
print(sum_of_even_numbers(3))