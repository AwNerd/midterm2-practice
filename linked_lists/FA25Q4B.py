"""Fall 2025 MT2 Q4(b) "Exclusive"

Implement exclude_link, which takes a linked list of numbers s and a number x.
It returns a linked list with all the elements of s that are not equal to x. The
input linked list should not be modified.

Exam:     https://cs61a.org/resources/fa25/mt2/61a-fa25-mt2.pdf
Solution: https://cs61a.org/resources/fa25/mt2/61a-fa25-mt2_sol.pdf
"""
import os, sys; sys.path[1:1] = [os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', d) for d in ('done', 'recursion', 'lists_and_dicts', 'linked_lists')]  # lets imports work from any folder
from link import Link

def exclude_link(s, x):
    """Return a linked list with all elements of linked list s except those equal to x.
    >>> a = Link(3, Link(4, Link(5, Link(3.0, Link(6, Link(5, Link(3)))))))
    >>> exclude_link(a, 3)
    Link(4, Link(5, Link(6, Link(5))))
    >>> a  # no change to a
    Link(3, Link(4, Link(5, Link(3.0, Link(6, Link(5, Link(3)))))))
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
