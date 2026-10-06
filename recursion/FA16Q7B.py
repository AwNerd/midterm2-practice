"""Fall 2016 MT2 Q7(b) "Summer Camp" (challenge)

Part (a) was a normal recursive sums(n, k): return a list of all the ways that a
list of k positive integers can sum to n.

Part (b): "Why so many lines?" Implement f and g for this alternative version of
sums. f and g must each be a single lambda expression (f is global and recursive;
g is defined inside sums and is recursive). The last line of sums is given.

Exam:     https://cs61a.org/resources/fa16/mt2/61a-fa16-mt2.pdf
Solution: https://cs61a.org/resources/fa16/mt2/61a-fa16-mt2_sol.pdf
"""

f = None  # replace with a one-line lambda of the form: lambda x, y: ...


def sums(n, k):
    """Return the ways in which K positive integers can sum to N.
    >>> sums(2, 2)
    [[1, 1]]
    >>> sums(4, 2)
    [[3, 1], [2, 2], [1, 3]]
    >>> sums(5, 3)
    [[3, 1, 1], [2, 2, 1], [2, 1, 2], [1, 3, 1], [1, 2, 2], [1, 1, 3]]
    """
    g = None  # replace with a one-line lambda of the form: lambda w: ...
    return [v for v in g(k) if sum(v) == n]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
