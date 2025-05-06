
"""
Problem:
Print numbers from 1000 down to 1 using recursion.
Constraints:
- Do not use for/while loops.
- Do not use range() or similar built-in iterators.

Approach:
- Increase recursion limit using sys.setrecursionlimit.
- Define recursive function to print from n down to 1.
"""

import sys
sys.setrecursionlimit(1100)  # Increase limit slightly beyond 1000

def reverse_count(n):
    if n == 0:
        return
    print(n)
    reverse_count(n - 1)

if __name__ == "__main__":
    reverse_count(1000)