"""Fall 2025 MT2 Q6(a) "Two Topping Pizzas"

Implement symmetrical, which takes a dictionary d and returns True if for every
pair (k, v) for which d[k] == v, it's also true that d[v] == k, and returns False
otherwise.

Exam:     https://cs61a.org/resources/fa25/mt2/61a-fa25-mt2.pdf
Solution: https://cs61a.org/resources/fa25/mt2/61a-fa25-mt2_sol.pdf
"""

def symmetrical(d):
    """Return whether every key-value pair in d is also a value-key pair.
    >>> symmetrical({'M': 'P', 'P': 'M', 'G': 'G'})
    True
    >>> symmetrical({'M': 'P', 'P': 'M', 'G': 'M'})  # No M->G
    False
    >>> symmetrical({'M': 'P', 'P': 'M', 'G': 'T'})  # No T->G
    False
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
