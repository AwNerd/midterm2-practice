"""Fall 2022 MT2 Q5(a) "Aim for 100"

count_subsets takes as input a list of positive integers s. It returns the
number of lists that sum to 100 and contain a subset of the elements of s in order.

(The original exam also had `count_subsets(list(range(1, 10000)))` -> 444793 as a
doctest; it's far too slow for the template's approach, so it's left out here.)

Exam:     https://cs61a.org/resources/fa22/mt2/61a-fa22-mt2.pdf
Solution: https://cs61a.org/resources/fa22/mt2/61a-fa22-mt2_sol.pdf
"""

def count_subsets(s):
    """
    >>> count_subsets([25, 50, 75, 100, 125, 150])  # [25, 75], [100]
    2
    >>> count_subsets([25, 50, 25, 75])  # [25, 75] (first 25), [25, 75] (second 25), [25, 50, 25]
    3
    """
    def helper(sum_so_far, index):
        if sum_so_far == 100:
            return 1
        if sum_so_far > 100 or index >= len(s):
            return 0
        else:
            return helper(sum_so_far + s[index], index + 1) + helper(sum_so_far, index + 1)
    return helper(0, 0)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
