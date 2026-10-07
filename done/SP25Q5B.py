"""Spring 2025 MT2 Q5(b) "Just Add and Multiply"

A plus-times-expression for a list (or linked list) of numbers inserts either
+ or * between each adjacent pair of numbers. (Normal precedence: * before +.)

Implement ways, which returns the number of possible plus-times-expressions for
a list of length n that have at most k *-symbols in a row.

Exam:     https://cs61a.org/resources/sp25/mt2/61a-sp25-mt2.pdf
Solution: https://cs61a.org/resources/sp25/mt2/61a-sp25-mt2_sol.pdf
"""

def ways(k, n):
    """Return the number of plus-times-expressions with at most k consecutive *'s
    for n numbers.
    >>> ways(1, 4)
    5
    >>> ways(2, 4)
    7
    >>> ways(2, 5)
    13
    """
    def f(left, n):
        if left < 0:
            return 0
        if n == 1:
            return 1
        else:
            return f(left - 1, n - 1) + f(k, n - 1)
    return f(k, n)



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
