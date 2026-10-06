"""Fall 2017 MT2 Q3(c) "Pumpkin Splice Latte"

Implement splink, which takes two Link instances a and b and a non-negative
integer k that is less than or equal to the length of a. It returns a Link instance
containing the first k elements of a, then all elements of b, then the remaining
elements of a.

Exam:     https://cs61a.org/resources/fa17/mt2/61a-fa17-mt2.pdf
Solution: https://cs61a.org/resources/fa17/mt2/61a-fa17-mt2_sol.pdf
"""
from link import Link

def splink(a, b, k):
    """Return a Link containing the first k elements of a, then all of b, then the rest of a.
    >>> splink(Link(2, Link(3, Link(4, Link(5)))), Link(6, Link(7)), 2)
    Link(2, Link(3, Link(6, Link(7, Link(4, Link(5))))))
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
