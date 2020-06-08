def is_prime(number: int):
    """Checks if number is prime
    
    Parameters:
    number (int): number for checking
    
    Returns:
    bool: True if number is prime, else False
    
    """
    
    if (number <= 1):
        return False
    if (number <= 3):
        return True
    if (number % 2 == 0 or number % 3 == 0):
        return False
    
    i = 5
    while(i * i <= number):
        if (number % i == 0 or number % (i + 2) == 0):
            return False
        i = i + 6
    return True
