#!/usr/bin/env python3
'''Task 9 - Duck type an iterable
'''
from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''returns length of list of parameters'''
    return [(i, len(i)) for i in lst]
