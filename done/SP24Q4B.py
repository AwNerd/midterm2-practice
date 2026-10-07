"""Spring 2024 MT2 Q4(b) "Who's counting?"

A strip is a list of integers in which each integer is one more than the last.
For example, [3, 4, 5, 6] is a strip. Empty and one-element lists are strips.

Implement drip, which takes two non-empty lists of integers s and t. It returns
True if there is a strip containing all and only the elements of s and t starting
with s[0] in which the elements of s appear in order and the elements of t appear
in order. It returns False otherwise. (is_strip from part (a) is imported.)

Exam:     https://cs61a.org/resources/sp24/mt2/61a-sp24-mt2.pdf
Solution: https://cs61a.org/resources/sp24/mt2/61a-sp24-mt2_sol.pdf
"""
import os, sys; sys.path[1:1] = [os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', d) for d in ('done', 'recursion', 'lists_and_dicts', 'linked_lists')]  # lets imports work from any folder
from SP24Q4A import is_strip

def drip(s, t):
    """Return whether there is a strip made out of interleaving s and t.
    >>> drip([1, 3, 5], [2, 4, 6])  # 1 2 3 4 5 6
    True
    >>> drip([1, 4, 5], [2, 3, 6])  # 1 2 3 4 5 6
    True
    >>> drip([1, 2, 3], [4, 5, 6])  # 1 2 3 4 5 6
    True
    >>> drip([2, 4, 5], [1, 3, 6])  # No strip starting with 2 can contain 1
    False
    >>> drip([1, 2, 4, 5], [1, 3, 6])  # No strip can contain 1 and 1
    False
    >>> drip([1, 4, 5], [2, 3, 7])  # No strip can contain 5 and 7 but no 6
    False
    >>> drip([1, 5, 4], [2, 3, 6])  # No strip can contain 5 before 4
    False
    >>> drip([2], [3, 4, 5])  # 2 3 4 5
    True
    >>> drip([1], [2, 3, 5])  # No strip can contain 3 and 5 but no 4
    False
    """
    t_counter, s_counter, curr = 0,1,s[0]
    while t_counter != len(t) and s_counter != len(s):
        if t[t_counter] == curr + 1:
            t_counter += 1
            curr += 1
        elif s[s_counter] == curr + 1:
            s_counter += 1
            curr += 1
        else:
            return False
    
    if t_counter != len(t):
        return t[t_counter] == curr + 1 and all([t[i] + 1 == t[i + 1] for i in range(t_counter, len(t) - 1)])
    else:
        return s[s_counter] == curr + 1 and all([s[i] + 1 == s[i + 1] for i in range(s_counter, len(s) - 1)])
        


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
