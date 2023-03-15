def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    return_dict = {}
    for char in phrase:
        char = char.lower()
        if char in "aeiou":
            return_dict[char] = return_dict[char] + \
                1 if return_dict.get(char, None) else 1
    return return_dict
