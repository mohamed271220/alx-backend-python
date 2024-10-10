#!/usr/bin/env python3
from typing import List

"""
This module defines a function that sums a list
"""


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floats to sum.

    Returns:
        float: The sum of the floats.
    """
    return sum(input_list)
