#!/usr/bin/env python3
'''Task 7 - complex types - string and int/float to tuple
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Takes in a key and its value and
    converts it to a tuple of the key and square of its value'''
    return (k, float(v**2))
