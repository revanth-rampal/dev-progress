def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    if n==1:
       return ['*']
    elif n==2 :
        return ['**', '**']
    else:
        square = [n* '*']
        for _ in range(n-2):
            square.append('*'+' '*(n-2)+'*')
        square.append(n*"*")
    return square