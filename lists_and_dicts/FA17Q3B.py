"""Fall 2017 MT2 Q3(b) "Pumpkin Splice Latte"

Implement all_splice, which returns a list of all the non-negative integers k
such that splicing list b into list a at k creates a list with the same contents as
c. (splice from part (a) is imported.)

Exam:     https://cs61a.org/resources/fa17/mt2/61a-fa17-mt2.pdf
Solution: https://cs61a.org/resources/fa17/mt2/61a-fa17-mt2_sol.pdf
"""
import os, sys; sys.path[1:1] = [os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', d) for d in ('done', 'recursion', 'lists_and_dicts', 'linked_lists')]  # lets imports work from any folder
from FA17Q3A import splice

def all_splice(a, b, c):
    """Return a list of all k such that splicing b into a at position k gives c.
    >>> all_splice([1, 2], [3, 4], [1, 3, 4, 2])
    [1]
    >>> all_splice([1, 2, 1, 2], [1, 2], [1, 2, 1, 2, 1, 2])
    [0, 2, 4]
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
