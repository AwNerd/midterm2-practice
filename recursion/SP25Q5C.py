"""Spring 2025 MT2 Q5(c) "Just Add and Multiply"

A plus-times-expression for a list (or linked list) of numbers inserts either
+ or * between each adjacent pair of numbers. (Normal precedence: * before +.)

Implement close, which takes a list of numbers s and a number x and returns the
value of a plus-times-expression for s that is closest to x.
(product is provided.)

Exam:     https://cs61a.org/resources/sp25/mt2/61a-sp25-mt2.pdf
Solution: https://cs61a.org/resources/sp25/mt2/61a-sp25-mt2_sol.pdf
"""

# ---- Provided by the exam (don't change) ----

def product(s):
    """Return the result of multiplying together the elements of a non-empty list of numbers s."""
    if len(s) == 1:
        return s[0]
    return s[0] * product(s[1:])

# ---- Your work ----

def close(s, x):
    """Return the value of a plus-times-expression for s closest to x.
    >>> print(close([1, 2, 3, 4], 10))  # 1 + 2 + 3 + 4
    10
    >>> print(close([1, 2, 3, 4], 20))  # 1 * 2 * 3 * 4
    24
    >>> print(close([1, 2, 3, 4], 30))  # 1 + 2 * 3 * 4
    25
    >>> print(close([3, 7, 5, 4, 2, 6], 66))
    67
    """
    
        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
