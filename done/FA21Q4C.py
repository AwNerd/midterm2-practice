"""Fall 2021 MT2 Q4(c) "Thanos"

Implement max_diff_fast, which has the same signature and behavior as max_diff
(part (b)), but has a faster order of growth of its run time.
You may not use a list comprehension. (Original: a single return line.)

Hint: you may call built-in sequence functions: sum, max, min, all, any, map, filter, zip, and reversed.

Exam:     https://cs61a.org/resources/fa21/mt2/61a-fa21-mt2.pdf
Solution: https://cs61a.org/resources/fa21/mt2/61a-fa21-mt2_sol.pdf
"""

def max_diff_fast(s, f):
    """Return two elements (v, w) of s for which f(v) - f(w) is largest.
    >>> max_diff_fast(range(-7, 4), lambda x: x * x)  # (-7 * -7) - (0 * 0) = 49
    (-7, 0)
    >>> max_diff_fast(['what', 'a', 'great', 'film'], len)  # len('great') - len('a')
    ('great', 'a')
    """
    curr = 0
    maxv, maxw = 0,0
    for v in s:
        for w in s:
            if f(v) - f(w) > curr:
                curr = f(v) - f(w)
                maxv, maxw = v, w
    return maxv, maxw

    



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
