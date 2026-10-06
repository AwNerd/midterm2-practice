"""Fall 2018 MT2 Q4(b) "Nonplussed"

A plus expression for a non-negative integer n is made by inserting + symbols
between digits of n, such that there are never more than two consecutive digits in
the resulting expression. E.g. for 2018: 2+0+1+8, 20+1+8, 2+0+18, 2+01+8, 20+18.
(A two-digit chunk may start with 0, like 01.)

Implement plusses, which takes non-negative integers n and cap. It returns the
number of plus expressions for n whose value is below cap.

Exam:     https://cs61a.org/resources/fa18/mt2/61a-fa18-mt2.pdf
Solution: https://cs61a.org/resources/fa18/mt2/61a-fa18-mt2_sol.pdf
"""

def plusses(n, cap):
    """Return the number of plus expressions for n with values below cap.
    >>> plusses(123, 16)  # 1+2+3=6 and 12+3=15, but 1+23=24 isn't below cap.
    2
    >>> plusses(2018, 38)  # 2+0+1+8, 20+1+8, 2+0+18, and 2+01+8, but not 20+18.
    4
    >>> plusses(1, 2)
    1
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
