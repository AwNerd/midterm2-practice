"""Fall 2014 MT2 Q3(b) "This One Goes to Eleven"

Implement no_eleven, a function that returns a list of all distinct length-n
lists of ones and sixes in which 1 and 1 do not appear consecutively.
(Order matters for the doctests: lists starting with 6 come first.)

Exam:     https://cs61a.org/resources/fa14/mt2/61a-fa14-mt2.pdf
Solution: https://cs61a.org/resources/fa14/mt2/61a-fa14-mt2_sol.pdf
"""

def no_eleven(n):
    """Return a list of lists of 1's and 6's that do not contain 1 after 1.
    >>> no_eleven(2)
    [[6, 6], [6, 1], [1, 6]]
    >>> no_eleven(3)
    [[6, 6, 6], [6, 6, 1], [6, 1, 6], [1, 6, 6], [1, 6, 1]]
    >>> no_eleven(4)[:4]
    [[6, 6, 6, 6], [6, 6, 6, 1], [6, 6, 1, 6], [6, 1, 6, 6]]
    >>> no_eleven(4)[4:]
    [[6, 1, 6, 1], [1, 6, 6, 6], [1, 6, 6, 1], [1, 6, 1, 6]]
    """
    if n == 0:
        return []
    else:
        using_six = [6] + no_eleven(n-1)
        using_one = [1] + no_eleven(n-1)
    for list in using_six:
        for i in range(0, len(list)):
            if list[i] == 1 and list[i+1] == 1:
                using_six.pop(list)
    
    for list in using_one:
        for i in range(0, len(list)):
            if list[i] == 1 and list[i+1] == 1:
                using_one.pop(list)

    return using_six + using_one


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
