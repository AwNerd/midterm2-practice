"""Fall 2015 MT2 Q3(e) "Return of the Digits" (challenge)

Implement int_set, which is a higher-order function that takes a list of
non-negative integers called contents. It returns a function that takes a
non-negative integer n and returns whether n appears in contents.

Clue: Every integer can be expressed uniquely as a sum of powers of 2. E.g., 5
equals 1 + 4 equals pow(2, 0) + pow(2, 2). The bits helper function (provided)
encodes a list of nums using sequences of 0's and 1's that tell you whether each
power of 2 is used, starting with pow(2, 0).

Restriction: you may not use built-in tests of list membership, such as an `in`
expression or a list's index method.

Exam:     https://cs61a.org/resources/fa15/mt2/61a-fa15-mt2.pdf
Solution: https://cs61a.org/resources/fa15/mt2/61a-fa15-mt2_sol.pdf
"""

# ---- Provided by the exam (don't change) ----

def bits(nums):
    """A set of nums represented as a function that takes 'entry', 0, or 1.
    >>> t = bits([4, 5])  # Contains 4 and 5, but not 2
    >>> t(0)(0)(1)('entry')  # 4 = 0 * pow(2, 0) + 0 * pow(2, 1) + 1 * pow(2, 2)
    True
    >>> t(0)(1)('entry')  # 2 = 0 * pow(2, 0) + 1 * pow(2, 1)
    False
    >>> t(1)(0)(1)('entry')  # 5 = 1 * pow(2, 0) + 0 * pow(2, 1) + 1 * pow(2, 2)
    True
    """
    def branch(last):
        if last == 'entry':
            return 0 in nums
        return bits([k // 2 for k in nums if k % 2 == last])
    return branch

# ---- Your work ----

def int_set(contents):
    """Return a function that represents a set of non-negative integers.
    >>> int_set([1, 2])(1), int_set([1, 2])(3)  # 1 in [1, 2] but 3 is not
    (True, False)
    >>> s = int_set([1, 3, 4, 7, 9])
    >>> [s(k) for k in range(10)]
    [False, True, False, True, True, False, False, True, False, True]
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    print("Done (no output above = all doctests passed).")
