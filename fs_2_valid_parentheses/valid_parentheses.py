def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    # parens = list(parens)
    # if len(parens) % 2 != 0:
    #     return False
    if parens[0] == ")":
        return False
    for i in range(len(parens)):
        if parens[i] == parens[-1-i]:
            return False
    return True
