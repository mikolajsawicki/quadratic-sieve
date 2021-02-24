from functools import reduce
from math import log
from typing import Tuple
from . import fast_gauss as fg
from .base import *
from .primes import *

loud = False


def qs_print(*args, **kwargs):
    """Calls print() only if loud mode is active.

    :param args:
    :param kwargs:
    :return:
    """
    if loud:
        print(*args, **kwargs)


def smoothness_bound(n: int) -> int:
    """Computes the optimal smoothness bound for n.

    Bases on "SMOOTH NUMBERS AND THE QUADRATIC SIEVE" by Carl Pomerance.

    :param n: number being factorized
    :return: smoothness bound number
    """
    x = ceil(log(n) * log(log(n)))
    x = x ** 0.5 * 0.5
    x = 2.71 ** x
    return ceil(x) + 1


def value(exp_vector: Sequence[int], primes: Sequence[int]) -> int:
    """Computes value of number represented by exponent vector over certain primes.

    :param exp_vector: list of exponents
    :param primes: primes list
    :return: value of represented number
    """
    if exp_vector == [0] * len(primes):
        return 0

    val = 1

    for prime, exp in zip(primes, exp_vector):
        val *= prime ** exp

    return val


def gcd(a: int, b: int) -> int:
    while b != 0:
        t = b
        b = a % b
        a = t

    return a


def congruent(a: int, b: int, n: int) -> bool:
    return a % n == b % n


def solve(base: Base) -> Union[Tuple[int, int], None]:
    n = base.n

    for rows in fg.perfect_square_combinations(base.x_sq_minus_n_exp):
        exp_vector = [0] * base.width

        for i in rows:
            exp_vector = [x + base.x_sq_minus_n_exp[i][j] for j, x in enumerate(exp_vector)]

        exp_vector = [x // 2 for x in exp_vector]

        v = value(exp_vector, base.primes)

        xes_prod = reduce(lambda x, y: x * y, [base.x[i] for i in rows])

        a = v % n
        b = xes_prod % n

        if not congruent(a, b, n) and not congruent(a, -b, n):
            factor = gcd(a - b, n)

            return factor, n // factor

    qs_print('Didn\'t find any nontrivial solution. Try changing the smoothness bound and base size.')
    return None


def factorize(n: int, b: Union[int, None] = None, base_size: Union[int, None] = None,
              primes: Union[List[int], None] = None, loud_mode: bool = False) -> Tuple[int, int]:
    """Finds factors of n using quadratic sieve algorithm with b-smooth base.

    :param n: number being factorized
    :param b: smoothness bound
    :param base_size: size of sieve's base
    :param primes: primes base to use
    :param loud_mode: True for displaying output information while work
    :return: tuple of n's factors or None
    """
    global loud
    loud = loud_mode

    if b is None:
        b = smoothness_bound(n)

    qs_print('Smoothness bound: ', b)

    if primes is None:
        qs_print('Loading primes base...')

        primes = get_smooth_primes(b)

        primes = [2] + [p for p in primes[1:] if legendre(n, p) == 1]

    qs_print('Primes in base: ', len(primes))

    if base_size is None:
        base_size = len(primes)

    qs_print('Generating the base...')
    base = Base(n, primes, base_size)
    qs_print('The base has been generated.')

    qs_print('Searching for the right combination...')

    return solve(base)
