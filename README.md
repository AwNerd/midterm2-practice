# CS 61A Midterm 2 Practice

Past-exam problems from the instructor's in-scope list, written as blank stubs so you can practice coding from scratch.

Every file has:
- the problem statement and any restrictions, plus links to the exam and solution PDFs
- the function signature(s) and the original docstring and doctests
- helper `def` lines when the exam template used an inner helper (signature only)
- exam-provided helpers (`product`, `bits`, `apply_to_all`) included in full

There's no skeleton code. You write the function bodies.

## Running the tests

```bash
python3 recursion/FA24Q4A.py          # run one problem's doctests
python3 -m doctest -v recursion/FA24Q4A.py   # verbose (run from inside the folder for linked lists)
```

When everything passes, the only output is the `Done` line.

Linked-list problems import `Link` from `linked_lists/link.py`, where `Link.empty = ()`. That means old doctests using `Link.empty` and new code using `()` both work.

Some files import from another part of the same question. For example, `FA17Q3B` uses `splice` from `FA17Q3A`, and `SP24Q4B` uses `is_strip` from `SP24Q4A`. Solve the earlier part first.

Files that import have a one-line `sys.path` shim above the import, so they still run after being moved into `done/` (and the imported file can be in its original folder or in `done/`). Keep `link.py` in `linked_lists/`.

## Problems

### recursion/
| File | Problem |
|---|---|
| FA24Q4A | Almost a Perfect Question: semiperfect numbers |
| SP25Q5B | Just Add and Multiply: count plus-times-expressions |
| SP25Q5C | Just Add and Multiply: closest expression value |
| FA23Q4A | A Perfect Question: sums of perfect squares |
| SP23Q5A | Parking: counting parking arrangements |
| FA22Q5A | Aim for 100: subsets summing to 100 |
| FA19Q6 | Best of Both: switching between two lists |
| FA18Q4A | Nonplussed: largest plus-expression sum |
| FA18Q4B | Nonplussed: count plus expressions under a cap |
| FA17Q4C | Both Ways: counting paths through actions |
| FA16Q7B | Summer Camp (challenge): recursive lambdas |
| FA14Q3B | This One Goes to Eleven: no adjacent 1s |

### lists_and_dicts/
| File | Problem |
|---|---|
| FA25Q4A | Exclusive: filter with a comprehension |
| FA25Q6A | Two Topping Pizzas: symmetrical dict |
| FA25Q6B | Two Topping Pizzas: acceptable pizza |
| SP24Q4A | Who's counting?: is_strip |
| SP24Q4B | Who's counting?: drip |
| SP23Q3A | Prefixes: prefix sums with slicing |
| FA21Q2B | Doctor Change: all subset sums |
| FA21Q4B | Thanos: max_diff |
| FA21Q4C | Thanos: max_diff_fast |
| FA19Q4 | Seek Once: stable |
| FA18Q2 | Lowest: smallest absolute values |
| FA17Q3A | Pumpkin Splice Latte: splice |
| FA17Q3B | Pumpkin Splice Latte: all_splice |
| FA15Q3E | Return of the Digits (challenge): int_set |

### linked_lists/
| File | Problem |
|---|---|
| FA25Q4B | Exclusive: exclude_link |
| SP25Q5A | Just Add and Multiply: muladd |
| FA24Q5 | How Long is this Exam?: longer + longest |
| FA23Q6 | After Party: after (with find helper) |
| SP23Q3B | Prefixes: tens |
| FA20Q2B | Yield, Fibonacci!: filter_index |
| FA17Q3C | Pumpkin Splice Latte: splink |
| FA17Q4A | Both Ways: both (sorted common value) |
| FA14Q3A | This One Goes to Eleven: sixty_ones |

## Notes
- FA22Q5A: the exam's `count_subsets(list(range(1, 10000)))` doctest was dropped because the template's approach is exponential.
- FA16Q7B: `f` and `g` are placeholders set to `None`. Replace each one with a one-line lambda.
- FA23Q6: in the exam, you could only fill in `find`'s base case and `after`'s final return, without using `if`/`and`/`or`/brackets.

## hard_problems/

Blank copies of the problems worth redoing cold: FA24Q4A, FA23Q4A, FA22Q5A, FA18Q4B, SP25Q5B, SP25Q5C, FA19Q6, SP24Q4B, FA24Q5. Your finished versions stay in `done/`.
