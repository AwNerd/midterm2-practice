"""Fall 2023 MT2 Q4(a) "A Perfect Question"

Implement fit, which takes positive integers total and n. It returns True or
False indicating whether there are n positive perfect squares that sum to total.

Exam:     https://cs61a.org/resources/fa23/mt2/61a-fa23-mt2.pdf
Solution: https://cs61a.org/resources/fa23/mt2/61a-fa23-mt2_sol.pdf
"""

def fit(total, n):
    """Return whether there are n positive perfect squares that sums to total.
    >>> [fit(4, 1), fit(4, 2), fit(4, 3), fit(4, 4)]
    [True, False, False, True]
    >>> [fit(12, n) for n in range(3, 8)]
    [True, True, False, True, False]
    >>> [fit(32, 2), fit(32, 3), fit(32, 4), fit(32, 5)]
    [True, False, False, True]
    """
    def f(total, n, k):
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
