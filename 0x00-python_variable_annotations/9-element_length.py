#!/usr/bin/env python3
"""
This module provides a function that returns a list of tuples
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an element from the input
    """
    return [(i, len(i)) for i in lst]
