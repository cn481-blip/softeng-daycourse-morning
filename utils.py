# Assorted utility functions

def add(a, b):
    """Return the sum of a and b, or None if inputs are invalid."""
    try:
        return a + b
    except Exception:
        return None


def is_even(n):
    """Return True if n is even, False if odd, str if a decimal, or None if not a number."""
    try:
        if n % 2 not in [0,1]:
            return "your number is a decimal"
    except Exception:
        pass
    try:
        return n % 2 == 0
    except Exception:
        return None


def to_uppercase(s):
    """Convert a string to uppercase, or return None if not a string."""
    try:
        return s.upper()
    except Exception:
        return None


def get_list_average(lst):
    """Return the average of a list of numbers, or None if invalid."""
    try:
        return sum(lst) / len(lst) if lst else None
    except Exception:
        return None
