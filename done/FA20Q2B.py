"""Fall 2020 MT2 Q2(b) "Yield, Fibonacci!"

For a linked list s, the index of an element is the number of times rest appears
in the smallest dot expression containing only s, rest, and first that evaluates to
that element. (So s.first is index 0, s.rest.first is index 1, etc.)

Implement filter_index, which returns a new Link of the elements whose index i
satisfies f(i).

Exam:     https://cs61a.org/resources/fa20/mt2/61a-fa20-mt2.pdf
Solution: https://cs61a.org/resources/fa20/mt2/61a-fa20-mt2_sol.pdf
"""
import os, sys; sys.path[1:1] = [os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', d) for d in ('done', 'recursion', 'lists_and_dicts', 'linked_lists')]  # lets imports work from any folder
from link import Link

def filter_index(f, s):
    """Return a Link containing the elements of Link s that have an index i for
    which f(i) is a true value.

    >>> powers = Link(1, Link(2, Link(4, Link(8, Link(16, Link(32))))))
    >>> filter_index(lambda x: x < 4, powers)
    Link(1, Link(2, Link(4, Link(8))))
    >>> filter_index(lambda x: x % 2 == 1, powers)
    Link(2, Link(8, Link(32)))
    """
    def helper(i, s):
        if s == ():
            return s
        if f(i):
            return Link(s.first, helper(i + 1, s.rest))
        else:
            return helper(i + 1, s.rest)
    return helper(0, s)



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
