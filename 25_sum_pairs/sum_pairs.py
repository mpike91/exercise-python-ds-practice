def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    max = len(nums) + 1
    return_tuple = ()
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if (i != j) and (nums[i] + nums[j] == goal) and (i < max) and (j < max):
                max = i if i > j else j
                return_tuple = (nums[i], nums[j])
    return return_tuple
