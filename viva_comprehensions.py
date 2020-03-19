from typing import List, Dict, Set, Callable
import enum
import math

class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param start: starting value of list
    :param stop: stopping value of list
    :param parity: specifies odd (= 0) or even values (= 1)
    :return: list of numbers in range(start,stop)
    """
    if parity == Parity.ODD:
        return [x for x in range(start,stop) if x % 2 != 0]
    elif parity == Parity.EVEN:
        return [x for x in range(start, stop) if x % 2 == 0]


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start: starting number in range(start,stop)
    :param stop: ending number (exclusive) in range(start,stop)
    :param strategy: a lambda function
    :return: a dictionary with integer being keys from range(start,stop) and values being lambda operations
    performed on each key, respectively
    """
    a = list(range(start,stop))
    b = {}
    for i in a:
        b[i]=strategy(i)
    return b


def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in: string
    :return: set of upper case letters
    """
    if val_in.islower():
        a = []
        for i in val_in:
            a.append(i.upper())
        return set(a)
    elif not val_in.isupper():
        a = []
        for i in val_in:
            if i.islower():
                a.append(i.upper())
        return set(a)
    elif val_in.isupper():
        return set()