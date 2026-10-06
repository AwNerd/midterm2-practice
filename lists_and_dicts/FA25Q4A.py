"""Fall 2025 MT2 Q4(a) "Exclusive"

Implement exclude, which takes a list of numbers s and a number x. It returns a
list with all the elements of s that are not equal to x. The input list should not
be modified. (Original: one-line list comprehension.)

Exam:     https://cs61a.org/resources/fa25/mt2/61a-fa25-mt2.pdf
Solution: https://cs61a.org/resources/fa25/mt2/61a-fa25-mt2_sol.pdf
"""

def exclude(s, x):
    """Return a list with all of the elements of s except those equal to x.
    >>> a = [3, 4, 5, 3.0, 6, 5, 3]
    >>> exclude(a, 3)
    [4, 5, 6, 5]
    >>> a  # no change to a
    [3, 4, 5, 3.0, 6, 5, 3]
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
