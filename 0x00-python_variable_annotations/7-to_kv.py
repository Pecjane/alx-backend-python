#!/usr/bin/env python3
'''Contains function to_kv'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Takes a string and an int OR float as arguments and returns a tuple'''
    z: float = v * v
    ans = (k, z)
    return ans
