def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    num_set = {1, num}
    num_range = list(range(2, num))
    for x in num_range:
        if num % x == 0:
            num_set.add(x)
    num_list = list(num_set)
    num_list.sort()
    return num_list
