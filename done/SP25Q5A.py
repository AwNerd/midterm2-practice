"""Spring 2025 MT2 Q5(a) "Just Add and Multiply"

A plus-times-expression for a list (or linked list) of numbers inserts either
+ or * between each adjacent pair of numbers. (Normal precedence: * before +.)

Implement muladd, which combines the numbers in a linked list by alternately
multiplying and adding (first *, then +, then *, ...), using normal precedence.

Exam:     https://cs61a.org/resources/sp25/mt2/61a-sp25-mt2.pdf
Solution: https://cs61a.org/resources/sp25/mt2/61a-sp25-mt2_sol.pdf
"""
import os, sys; sys.path[1:1] = [os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', d) for d in ('done', 'recursion', 'lists_and_dicts', 'linked_lists')]  # lets imports work from any folder

def muladd(s):
    """Combine the numbers in linked list s by alternately multiplying and adding.
    >>> example = Link(9, Link(4, Link(7, Link(2, Link(0)))))  # (9 4 7 2 0)
    >>> muladd(example)  # 9 * 4 + 7 * 2 + 0, not 9 * (4 + 7 * (2 + 0))
    50
    >>> muladd(Link(2, example))  # 2 * 9 + 4 * 7 + 2 * 0
    46
    >>> muladd(Link(2))
    2
    """
    if s == ():
        return 0
    if s.rest == ():
        return s.first
    return s.first * s.rest.first + muladd(s.rest.rest)



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
