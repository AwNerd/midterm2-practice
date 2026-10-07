"""Fall 2017 MT2 Q4(a) "Both Ways"

Implement both, which takes two sorted linked lists composed of Link objects and
returns whether some value is in both of them.

Exam:     https://cs61a.org/resources/fa17/mt2/61a-fa17-mt2.pdf
Solution: https://cs61a.org/resources/fa17/mt2/61a-fa17-mt2_sol.pdf
"""
import os, sys; sys.path[1:1] = [os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', d) for d in ('done', 'recursion', 'lists_and_dicts', 'linked_lists')]  # lets imports work from any folder
from link import Link

def both(a, b):
    """Return whether there is any value that appears in both a and b, two sorted Link instances.
    >>> both(Link(1, Link(3, Link(5, Link(7)))), Link(2, Link(4, Link(6))))
    False
    >>> both(Link(1, Link(3, Link(5, Link(7)))), Link(2, Link(7, Link(9))))
    True
    >>> both(Link(1, Link(4, Link(5, Link(7)))), Link(2, Link(4, Link(5))))
    True
    """
    if a == () or b == ():
        return False
    if a.first == b.first:
        return True
    else:
        return any([both(a, b.rest), both(a.rest, b)])


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
