def binary_to_decimal(binary_str):
    """
    Function to convert a binary string to its decimal integer representation.
    
    Parameters:
    binary_str (str): The binary string to convert.
    
    Returns:
    int: The decimal representation of the binary string.
    """
    # Your code here
    if int(binary_str) == 0:
        return 0 
    dic = 0
    for i in binary_str:
        dic=dic*2+int(i)
    return dic 
