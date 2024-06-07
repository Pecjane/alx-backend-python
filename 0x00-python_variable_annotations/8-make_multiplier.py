#!/usr/bin/env python3
'''Contains function make_multiplier'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Make Multiplier """
    def multiply(value: float) -> float:
        """Multiply"""
        return value * multiplier
    return multiply
