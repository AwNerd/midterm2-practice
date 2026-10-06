"""Fall 2018 MT2 Q2 "Lowest"

Implement lowest, which takes a list of numbers s and returns a list of only the
elements of s with the smallest absolute value.
(Original: a single return line with a comprehension and min.)

Exam:     https://cs61a.org/resources/fa18/mt2/61a-fa18-mt2.pdf
Solution: https://cs61a.org/resources/fa18/mt2/61a-fa18-mt2_sol.pdf
"""

def lowest(s):
    """Return a list of the elements in s with the smallest absolute value.
    >>> lowest([3, -2, 2, -3, -4, 2, 3, 4])
    [-2, 2, 2]
    >>> lowest(range(-5, 5))
    [0]
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
