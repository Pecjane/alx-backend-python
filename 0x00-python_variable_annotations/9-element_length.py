#!/usr/bin/env python3
'''Duck types'''

from typing import Sequence, Tuple, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''element_length'''
    return [(i, len(i)) for i in lst]
