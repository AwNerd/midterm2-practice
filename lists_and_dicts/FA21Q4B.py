"""Fall 2021 MT2 Q4(b) "Thanos"

Implement max_diff, which takes a non-empty sequence s and a one-argument
function f. It returns a pair of elements (v, w) in s for which f(v) - f(w) is
largest. v and w may be the same or different elements of s.

Hint: you may call built-in sequence functions: sum, max, min, all, any, map, filter, zip, and reversed.

Exam:     https://cs61a.org/resources/fa21/mt2/61a-fa21-mt2.pdf
Solution: https://cs61a.org/resources/fa21/mt2/61a-fa21-mt2_sol.pdf
"""

def max_diff(s, f):
    """Return two elements (v, w) of s for which f(v) - f(w) is largest.
    >>> max_diff(range(-7, 4), lambda x: x * x)  # (-7 * -7) - (0 * 0) = 49
    (-7, 0)
    >>> max_diff(['what', 'a', 'great', 'film'], len)  # len('great') - len('a')
    ('great', 'a')
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
