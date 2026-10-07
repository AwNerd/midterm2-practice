"""Fall 2019 MT2 Q4 "Seek Once"

Implement stable, which takes a list of numbers s, a positive integer k, and a
non-negative number n. It returns whether all pairs of values in s with indices that
differ by at most k have an absolute difference in value of at most n.

Restriction: you may not use lambda, if, and, or or in your solution.

Exam:     https://cs61a.org/resources/fa19/mt2/61a-fa19-mt2.pdf
Solution: https://cs61a.org/resources/fa19/mt2/61a-fa19-mt2_sol.pdf
"""

def stable(s, k, n):
    """Return whether all pairs of elements of S within distance K differ by at most N.
    >>> stable([1, 2, 3, 5, 6], 1, 2)  # All adjacent values differ by at most 2.
    True
    >>> stable([1, 2, 3, 5, 6], 2, 2)  # abs(5-2) is a difference of 3.
    False
    >>> stable([1, 5, 1, 5, 1], 2, 2)  # abs(5-1) is a difference of 4.
    False
    """
    return  all([abs(s[i] - y) <= n for i in range(len(s)) for y in s[i + 1: k + i + 1]])


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
