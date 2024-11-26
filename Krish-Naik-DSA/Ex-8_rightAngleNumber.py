def generate_number_triangle(n):
    """
    Function to return a right-angled triangle of repeated numbers of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    pattern =[]
    for i in range (1,n+1):
        num = f'{i}'*i
        pattern.append(num)
    return pattern
print(generate_number_triangle(5))