def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    # Your code here
    pattern = []

    # Upper part
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        pattern.append(spaces + stars + spaces)

    # Lower part
    for j in range(n - 1):
        spaces = ' ' * (j + 1)
        stars = '*' * (2 * (n - j - 2) + 1)
        pattern.append(spaces + stars + spaces)

    return pattern