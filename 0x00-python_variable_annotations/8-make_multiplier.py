#!/usr/bin/env python3
from typing import Callable

"""
This module provides a function to create a multiplier function.
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to use in the returned function.

    Returns:
        Callable[[float], float]: A function that multiplies a float by multiplier.
    """

    def multiplier_function(n: float) -> float:
        """
        Multiplies the given number by the stored multiplier.

        Args:
            n (float): The number to be multiplied.

        Returns:
            float: The result of multiplying n by the multiplier.
        """
        return n * multiplier

    return multiplier_function
