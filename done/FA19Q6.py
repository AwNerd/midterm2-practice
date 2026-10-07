"""Fall 2019 MT2 Q6 "Best of Both"

A switch list r for two source lists s and t, both of length n, is a list where
each element r[i] for 0 <= i < n is either s[i] or t[i].

The switch count for r is the number of indices i for which r[i] and r[i-1] come
from different lists. As a special case, index 0 contributes 0 to the switch count
if r[0] comes from s and 1 if it comes from t.

Implement switch, which takes two lists of numbers s and t that have the same
length, and a non-negative integer k. It returns the switch list for s and t that
has the largest sum and has a switch count of at most k.

Exam:     https://cs61a.org/resources/fa19/mt2/61a-fa19-mt2.pdf
Solution: https://cs61a.org/resources/fa19/mt2/61a-fa19-mt2_sol.pdf
"""

def switch(s, t, k):
    """Return the list with the largest sum built by switching between S and T at most K times.
    >>> switch([1, 2, 7], [3, 4, 5], 0)
    [1, 2, 7]
    >>> switch([1, 2, 7], [3, 4, 5], 1)
    [3, 4, 5]
    >>> switch([1, 2, 7], [3, 4, 5], 2)
    [3, 4, 7]
    >>> switch([1, 2, 7], [3, 4, 5], 3)
    [3, 4, 7]
    """
    if k == 0:
        return s
    if not s or not t:
        return []
    else:
        return max([s[0]] + switch(s[1:], t[1:], k), [t[0]] + switch(t[1:], s[1:], k - 1), key=sum)
        


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
