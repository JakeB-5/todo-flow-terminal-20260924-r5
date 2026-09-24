"""Utilities for working with lists."""


def chunked(values, size):
    """Return new, ordered list chunks of at most size elements.

    size must be a positive integer, excluding bool. Elements are not
    deep-copied, and the input list is left unchanged.
    """
    if isinstance(size, bool) or not isinstance(size, int) or size <= 0:
        raise ValueError("size must be a positive integer excluding bool")
    return [values[start:start + size] for start in range(0, len(values), size)]
