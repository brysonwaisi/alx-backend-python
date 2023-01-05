#!/usr/bin/env python3
'''Task 6 - complex types - mixed
'''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''Takes a list mxd_lst of integers and floats
    returns their sum as a float.'''
    return float(sum(mxd_list))
