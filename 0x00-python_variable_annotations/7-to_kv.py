#!/usr/bin/env python3
"""
This module provides a function to create tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a key and its value to a tuple of the key"""
    return (k, float(v**2))
