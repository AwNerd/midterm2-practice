"""Spring 2024 MT2 Q4(a) "Who's counting?"

A strip is a list of integers in which each integer is one more than the last.
For example, [3, 4, 5, 6] is a strip. Empty and one-element lists are strips.

Implement is_strip.

Exam:     https://cs61a.org/resources/sp24/mt2/61a-sp24-mt2.pdf
Solution: https://cs61a.org/resources/sp24/mt2/61a-sp24-mt2_sol.pdf
"""

def is_strip(s):
    """Return whether list s is a strip.
    >>> is_strip([3, 4, 5, 6])
    True
    >>> is_strip([3, 3, 3])  # 3 after 3
    False
    >>> is_strip([3, 4, 5, 4, 6])  # 4 after 5
    False
    >>> is_strip([3, 4, 5, 5, 6])  # 5 after 5
    False
    >>> is_strip([3, 4, 5, 6, 8])  # 8 after 6
    False
    >>> is_strip([5])
    True
    >>> is_strip([])
    True
    """
    return all([s[i] + 1 == s[i+1] or s == list for i in range(len(s) - 1)])

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
