def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase = ""
    upper = to_swap.upper()
    lower = to_swap.lower()
    for char in phrase:
        if char == upper:
            new_phrase += lower
        elif char == lower:
            new_phrase += upper
        else:
            new_phrase += char
    return new_phrase
