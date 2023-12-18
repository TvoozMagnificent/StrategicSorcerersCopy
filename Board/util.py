
from typing import Union

def rank(i: int) -> int:
    """
    Convert an id into a rank number
    :param i: an id 0~7 denoting ranks 1~8
    :return: the rank i denotes
    """
    assert i in [0, 1, 2, 3, 4, 5, 6, 7] # i does not match expected range
    return 8 - i

def file(i: int) -> str:
    """
    Convert an id into a file letter
    :param i: an id 0~7 denoting files a~h
    :return: the file i denotes
    """
    assert i in [0, 1, 2, 3, 4, 5, 6, 7] # i does not match expected range
    return "abcdefgh"[i]

def id(i: Union[int, str]) -> int:
    """
    Convert a rank or file into an id
    :param i: a rank 1~8 or a file a~h
    :return: the id i denotes (0~7)
    """
    if isinstance(i, int):
        assert i in [1, 2, 3, 4, 5, 6, 7, 8] # i does not match expected range
        return 8 - i
    elif isinstance(i, str):
        assert i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] # i does not match expected range
        return ord(i) - ord('a')
    assert False # i does not match expected range
