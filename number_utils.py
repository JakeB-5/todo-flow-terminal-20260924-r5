"""Utilities for working with numbers."""


def clamp(value, lower, upper):
    """Limit value to the closed interval, rejecting reversed bounds."""
    if lower > upper:
        raise ValueError("lower must not exceed upper")
    if value < lower:
        return lower
    if value > upper:
        return upper
    return value
