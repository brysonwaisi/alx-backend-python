#!/usr/bin/env python3
'''Task 8 - complex types - functions
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Function creates multipier function'''
    return lambda x: x * multiplier
