"""Fall 2018 MT2 Q4(a) "Nonplussed"

A plus expression for a non-negative integer n is made by inserting + symbols
between digits of n, such that there are never more than two consecutive digits in
the resulting expression. E.g. for 2018: 2+0+1+8, 20+1+8, 2+0+18, 2+01+8, 20+18.
(A two-digit chunk may start with 0, like 01.)

Implement plus, which returns the largest sum from any plus expression for n.

Exam:     https://cs61a.org/resources/fa18/mt2/61a-fa18-mt2.pdf
Solution: https://cs61a.org/resources/fa18/mt2/61a-fa18-mt2_sol.pdf
"""

def plus(n):
    """Return the largest sum that results from inserting +'s into n.
    >>> plus(123456)  # 12 + 34 + 56 = 102
    102
    >>> plus(1604)  # 1 + 60 + 4 = 65
    65
    >>> plus(160450)  # 1 + 60 + 4 + 50 = 115
    115
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
