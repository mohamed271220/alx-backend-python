#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple

"""
This module provides a function that returns a list of tuples
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an element from the input
    iterable and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples with each element and its length.
    """
    return [(i, len(i)) for i in lst]
