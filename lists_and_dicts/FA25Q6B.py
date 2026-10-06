"""Fall 2025 MT2 Q6(b) "Two Topping Pizzas"

Implement acceptable, which takes a non-empty string pizza and a symmetrical
dictionary of strings disallow. Each character of pizza is one slice's topping
(_ means no topping), and the pizza is round, so the last slice is next to the
first. It returns whether no slice that is next to another slice appears with it
as a key-value pair in disallow. (symmetrical from part (a) is imported.)

Exam:     https://cs61a.org/resources/fa25/mt2/61a-fa25-mt2.pdf
Solution: https://cs61a.org/resources/fa25/mt2/61a-fa25-mt2_sol.pdf
"""
import os, sys; sys.path[1:1] = [os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', d) for d in ('done', 'recursion', 'lists_and_dicts', 'linked_lists')]  # lets imports work from any folder
from FA25Q6A import symmetrical

def acceptable(pizza, disallow={'M': 'P', 'P': 'M'}):
    """Return whether there are no slices next to each other with a disallowed topping pair.
    >>> acceptable("MM_PPP__M")
    True
    >>> acceptable("MM__PPP")  # The first slice M and last slice P are next to each other.
    False
    >>> acceptable("MM__PPP_")
    True
    >>> acceptable("MM__MPPP_")
    False
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
