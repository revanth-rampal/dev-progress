def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.

    Parameters:
    n (int): The height of the pyramid.

    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    """
    pattern = []
    for i in range(1, n + 1):
        # Create spaces for alignment
        space = ' ' * (n - i)
        # Create the number sequence for the row, separated by spaces
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        # Combine spaces and numbers
        pattern.append(space + numbers + space)
    return pattern

# Example Usage
print(generate_number_pyramid(4))