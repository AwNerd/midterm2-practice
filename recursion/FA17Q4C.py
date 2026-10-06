"""Fall 2017 MT2 Q4(c) "Both Ways"

Implement ways, which takes two values start and end, a non-negative integer k,
and a list of one-argument functions actions. It returns the number of ways of
choosing functions f1, f2, ..., fj from actions, such that f1(f2(...(fj(start))))
equals end and j <= k. The same action function can be chosen multiple times. If a
sequence of actions reaches end, then no further actions can be applied.

Exam:     https://cs61a.org/resources/fa17/mt2/61a-fa17-mt2.pdf
Solution: https://cs61a.org/resources/fa17/mt2/61a-fa17-mt2_sol.pdf
"""

def ways(start, end, k, actions):
    """Return the number of ways of reaching end from start by taking up to k actions.
    >>> ways(-1, 1, 5, [abs, lambda x: x+2])  # abs(-1) or -1+2, but not abs(abs(-1))
    2
    >>> ways(1, 10, 5, [lambda x: x+1, lambda x: x+4])  # 1+1+4+4, 1+4+4+1, or 1+4+1+4
    3
    >>> ways(1, 20, 5, [lambda x: x+1, lambda x: x+4])
    0
    >>> ways([3], [2, 3, 2, 3], 4, [lambda x: [2]+x, lambda x: 2*x, lambda x: x[:-1]])
    3
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
