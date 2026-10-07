"""Fall 2024 MT2 Q5 "How Long is this Exam?"

(a) Implement longer: return the longer linked list, s or t. (Same length? return s.)

(b) A sublist of a linked list s is a linked list with some (or none or all) of
the elements of s in order. Implement longest: return the longest sublist of s that
sums to n or less. Do not mutate s. In case of a tie, return any of the longest
sublists whose sum is n or less. Assume the sum of the elements of Link.empty is 0.
Link.empty is a sublist of any linked list.

Exam:     https://cs61a.org/resources/fa24/mt2/61a-fa24-mt2.pdf
Solution: https://cs61a.org/resources/fa24/mt2/61a-fa24-mt2_sol.pdf
"""
import os, sys; sys.path[1:1] = [os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', d) for d in ('done', 'recursion', 'lists_and_dicts', 'linked_lists')]  # lets imports work from any folder
from link import Link

def longer(s, t):
    """Return the longer linked list, s or t. (Same length? return s.)
    >>> longer(Link(2, Link(3)), Link.empty)
    Link(2, Link(3))
    >>> longer(Link(2, Link(3)), Link(4, Link(5)))
    Link(2, Link(3))
    >>> longer(Link(2, Link(3)), Link(4, Link(5, Link(6, Link(7)))))
    Link(4, Link(5, Link(6, Link(7))))
    >>> longer(Link.empty, Link.empty) is Link.empty
    True
    """
    def helper(s_iterator, t_iterator):
        if s_iterator == () and t_iterator == ():
            return s
        if s_iterator == ():
            return t
        if t_iterator == ():
            return s
        else:
            return helper(s_iterator.rest, t_iterator.rest)
    return helper(s,t)


def longest(s, n):
    """Return the longest sublist of s that sums to n or less.
    >>> longest(Link(5, Link(1, Link(3, Link(4, Link(2, Link(7)))))), 7)
    Link(1, Link(3, Link(2)))
    >>> longest(Link(5, Link(1, Link(3, Link(4, Link(2, Link(7)))))), 70)
    Link(5, Link(1, Link(3, Link(4, Link(2, Link(7))))))
    >>> longest(Link(3, Link(4, Link(5))), 2) is Link.empty
    True
    """
    if s is Link.empty:
        return s
    t = longest(s.rest, n)
    if n - s.first >= 0:
        return longer(Link(s.first, longest(s.rest, n - s.first)), t)
    else:
        return t
    


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
