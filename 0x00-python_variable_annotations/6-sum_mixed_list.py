#!/usr/bin/env python3
"""
This module defines a function that sums a list
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats to sum.

    Returns:
        float: The sum of the integers and floats.
    """
    return sum(mxd_lst)
