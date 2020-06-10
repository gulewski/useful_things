def list_flatten(lst: list):
    """Flattens a list
    
    Parameters:
    lst (int): list for flattening
    
    Returns:
    generator object which contains flattened list
    
    Example:
    Input: 
    lst = [1, 2, [3, [4, 5], 4, 8], 9]
    Oulut: 
    list_flatten(lst) == <generator object list_flatten at 0x...>
    list(list_flatten(lst)) == [1, 2, 3, 4, 5, 4, 8, 9]
    
    """
    while lst:
        sublist = lst.pop(0)
        if isinstance(sublist, list):
            lst = sublist + lst
        else:
            yield sublist
