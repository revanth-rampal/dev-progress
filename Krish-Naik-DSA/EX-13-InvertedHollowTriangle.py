def generate_hollow_inverted_right_angled_triangle(n):
    """
    Function to return a hollow inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    pattern=[]
    for i in range(1,n+1):
        if i ==1:
            pattern.append("*"*(n))
        elif i==n:
            pattern.append('*')
        else:
            row = '*'+' '*(n-i-1)+'*'
            pattern.append(row)
    return pattern
print(generate_hollow_inverted_right_angled_triangle(4))