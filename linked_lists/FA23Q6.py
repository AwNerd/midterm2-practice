"""Fall 2023 MT2 Q6(a)-(b) "After Party"

Implement after, which takes a linked list s and values a and b. It returns
whether an element of s equal to b appears after an element of s equal to a.

The exam's version uses a helper find(s, n, f) that searches s for n and, if it
finds it, calls f on the rest of the list after it.
Restriction: you may not use or, and, if, [, or ] in after's return expression
(the original only lets you write the find helper's base case and the final return).

Exam:     https://cs61a.org/resources/fa23/mt2/61a-fa23-mt2.pdf
Solution: https://cs61a.org/resources/fa23/mt2/61a-fa23-mt2_sol.pdf
"""
from link import Link

def after(s, a, b):
    """Return whether b comes after a in linked list s.
    >>> t = Link(3, Link(6, Link(5, Link(4))))
    >>> after(t, 6, 4)
    True
    >>> after(t, 4, 6)
    False
    >>> after(t, 6, 6)
    False
    """
    def find(s, n, f):
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
