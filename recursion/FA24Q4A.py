"""Fall 2024 MT2 Q4(a) "Almost a Perfect Question"

A proper divisor of integer n is an integer d less than n that evenly divides n.
A semiperfect number is a positive integer equal to the sum of some (or all) of
its proper divisors.

Exam:     https://cs61a.org/resources/fa24/mt2/61a-fa24-mt2.pdf
Solution: https://cs61a.org/resources/fa24/mt2/61a-fa24-mt2_sol.pdf
"""

def semiperfect(n):
    """Return whether positive integer n is a sum of some (or all) of its proper divisors.
    >>> [k for k in range(1, 40) if semiperfect(k)]
    [6, 12, 18, 20, 24, 28, 30, 36]
    """
    
    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
