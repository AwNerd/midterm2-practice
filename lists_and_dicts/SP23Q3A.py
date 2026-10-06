"""Spring 2023 MT2 Q3(a) "Prefixes"

A prefix sum of a sequence of numbers is the sum of the first n elements for
some positive length n. (Original: one-line list comprehension using slicing.)

Exam:     https://cs61a.org/resources/sp23/mt2/61a-sp23-mt2.pdf
Solution: https://cs61a.org/resources/sp23/mt2/61a-sp23-mt2_sol.pdf
"""

def prefix(s):
    """Return a list of all prefix sums of list s.
    >>> prefix([1, 2, 3, 0, 4, 5])
    [1, 3, 6, 6, 10, 15]
    >>> prefix([2, 2, 2, 0, -5, 5])
    [2, 4, 6, 6, 1, 6]
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
