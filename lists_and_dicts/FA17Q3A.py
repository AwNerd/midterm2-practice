"""Fall 2017 MT2 Q3(a) "Pumpkin Splice Latte"

Implement splice, which takes two lists a and b and a non-negative integer k
that is less than or equal to the length of a. It returns the result of splicing b
into a at k.

Exam:     https://cs61a.org/resources/fa17/mt2/61a-fa17-mt2.pdf
Solution: https://cs61a.org/resources/fa17/mt2/61a-fa17-mt2_sol.pdf
"""

def splice(a, b, k):
    """Return a list of the first k elements of a, then all of b, then the rest of a.
    >>> splice([2, 3, 4, 5], [6, 7], 2)
    [2, 3, 6, 7, 4, 5]
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
