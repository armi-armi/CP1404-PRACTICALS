"""
CP1404/CP5632 Practical
Recursion
"""

def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)

# Expected output for do_it(5):
# 1 + 0 + 1 + 0 + 1 = 3
# Output should be 3.
print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n >= 0:  # Fix to only consider non-negative values
        print(n ** 2)
        do_something(n - 1)

# Expected output for do_something(4):
# 16, 9, 4, 1, 0
do_something(4)
