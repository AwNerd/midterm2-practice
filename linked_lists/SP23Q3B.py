"""Spring 2023 MT2 Q3(b) "Prefixes"

A prefix sum of a sequence of numbers is the sum of the first n elements for
some positive length n. Implement tens, which prints all prefix sums of a
(non-empty) linked list s that are multiples of ten, in order.

Exam:     https://cs61a.org/resources/sp23/mt2/61a-sp23-mt2.pdf
Solution: https://cs61a.org/resources/sp23/mt2/61a-sp23-mt2_sol.pdf
"""
import os, sys; sys.path[1:1] = [os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', d) for d in ('done', 'recursion', 'lists_and_dicts', 'linked_lists')]  # lets imports work from any folder
from link import Link

def tens(s):
    """Print all prefix sums of Link s that are multiples of ten.
    >>> tens(Link(3, Link(9, Link(8, Link(10, Link(0, Link(14, Link(6))))))))
    20
    30
    30
    50
    """
    



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
