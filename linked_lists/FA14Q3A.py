"""Fall 2014 MT2 Q3(a) "This One Goes to Eleven"

Implement sixty_ones, a function that takes a Link instance representing a
sequence of integers and returns the number of times that 6 and 1 appear
consecutively (a 1 directly after a 6). apply_to_all is provided.

Exam:     https://cs61a.org/resources/fa14/mt2/61a-fa14-mt2.pdf
Solution: https://cs61a.org/resources/fa14/mt2/61a-fa14-mt2_sol.pdf
"""
from link import Link

# ---- Provided by the exam (don't change) ----

def apply_to_all(map_fn, s):
    """Apply map_fn to each element of s.
    >>> apply_to_all(lambda x: x*3, range(5))
    [0, 3, 6, 9, 12]
    """
    return [map_fn(x) for x in s]

# ---- Your work ----

def sixty_ones(s):
    """Return the number of times that 1 follows 6 in linked list s.
    >>> once = Link(4, Link(6, Link(1, Link(6, Link(0, Link(1))))))
    >>> twice = Link(1, Link(6, Link(1, once)))
    >>> thrice = Link(6, twice)
    >>> apply_to_all(sixty_ones, [Link.empty, once, twice, thrice])
    [0, 1, 2, 3]
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
