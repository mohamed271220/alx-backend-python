#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""
from typing import Callable


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a multiplier function."""
    return lambda x: x * multiplier
