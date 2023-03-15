def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase_list = phrase.lower().split(" ")
    return_str = ""
    for str in phrase_list:
        return_str += str.capitalize() + " "
    return return_str.strip()
