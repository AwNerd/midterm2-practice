"""Spring 2023 MT2 Q5(a) "Parking"

When parking vehicles in a row, a motorcycle takes up 1 parking spot and a car
takes up 2 adjacent parking spots. A string of length n can represent n adjacent
parking spots using % for a motorcycle, <> for a car, and . for an empty spot.
E.g. '.%%.<><>' is an empty spot, two motorcycles, another empty spot, then two cars.

Implement count_park, which returns the number of ways to fill n adjacent spots.

Exam:     https://cs61a.org/resources/sp23/mt2/61a-sp23-mt2.pdf
Solution: https://cs61a.org/resources/sp23/mt2/61a-sp23-mt2_sol.pdf
"""

def count_park(n):
    """Count the ways to park cars and motorcycles in n adjacent spots.
    >>> count_park(1)  # '.' or '%'
    2
    >>> count_park(2)  # '..', '.%', '%.', '%%', or '<>'
    5
    >>> count_park(4)  # some examples: '<><>', '.%%.', '%<>%', '%.<>'
    29
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
