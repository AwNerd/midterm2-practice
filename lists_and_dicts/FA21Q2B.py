"""Fall 2021 MT2 Q2(b) "Doctor Change"

Part (a) defined change(n, coins), which returns whether there is a subset of
the values in coins that sums to n. E.g. change(10, [2, 7, 1, 8, 2]) is True (2+8),
change(6, [2, 7, 1, 8, 2]) is False.

Implement amounts, which takes a list of positive integers coins. It returns a
sorted list of all unique non-negative integers n for which change(n, coins)
returns True. You may not call change.

Exam:     https://cs61a.org/resources/fa21/mt2/61a-fa21-mt2.pdf
Solution: https://cs61a.org/resources/fa21/mt2/61a-fa21-mt2_sol.pdf
"""

def amounts(coins):
    """List all unique n such that change(n, coins) returns True (in sorted order).
    >>> amounts([2, 5, 3])
    [0, 2, 3, 5, 7, 8, 10]
    >>> amounts([2, 7, 1, 8, 2])
    [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20]
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
