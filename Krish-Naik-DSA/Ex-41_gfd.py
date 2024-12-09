def gcd(n, m):
    """
    Function to find the GCD of two integers without using built-in functions and recursion.
    
    Parameters:
    n (int): The first integer.
    m (int): The second integer.
    
    Returns:
    int: The GCD of n and m.
    """
    # Your code here
    list=[]
    for i in range(1,min(n,m)+1):
        if n%i==0 and m%i ==0:
            list.append(i)
    return max(list) 
print(gcd(48,18))