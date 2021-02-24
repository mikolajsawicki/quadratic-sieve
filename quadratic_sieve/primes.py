from distutils.sysconfig import get_python_lib
from typing import Union, List, Sequence
import os

if os.path.isfile(get_python_lib() + "/plateDetect"):
    BASE_DIR = get_python_lib() + "/plateDetect"
else:
    BASE_DIR = os.path.dirname(__file__)

PRIMES_URI = BASE_DIR + "/primes.txt"


def legendre(a: int, p: int) -> int:
    """Compute the Legendre symbol a|p using Euler's criterion.

    :param a:
    :param p: Odd prime.
    :return: 0 if a is divisible by b, 1 if a has a square root modulo p, 1 otherwise
    """

    if p % 2 == 0:
        raise ValueError('p should be an odd prime.')

    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls


def factorize(n: int, primes: Sequence[int]) -> Union[List[int], None]:
    """Factorizes n using only given primes.

    Returns exponent vector of n.
    If that's not possible, returns None.

    :param n: number to factorize
    :param primes: list of primes
    :return: exponent vector or None
    """
    exp = [0] * len(primes)

    if n == 0:
        return exp

    for i, p in enumerate(primes):
        while n % p == 0:
            exp[i] += 1
            n /= p

        if n <= 1:
            return exp

    return None


def get_smooth_primes(b: int = None) -> List[int]:
    """Loads primes list from the built-in txt base.

    :param b: The smoothness bound of primes to load.
    :return: List of primes.
    """

    primes = []

    with open(PRIMES_URI, 'r') as file:
        for line in file:
            for s in line.split():
                if not s.isnumeric():
                    continue

                p = int(s)

                if b is not None and p > b:
                    return primes

                primes.append(int(s))

    return primes
