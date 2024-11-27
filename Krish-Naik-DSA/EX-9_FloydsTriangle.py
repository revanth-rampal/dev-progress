def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle
    """
    # Your code here
    pattern = []
    num = 1
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append(str(num))
            num += 1
        pattern.append(" ".join(row))
    return pattern

print(generate_floyds_triangle(5))