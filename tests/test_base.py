from quadratic_sieve.base import *
from unittest import TestCase


class TestBase(TestCase):

    def test_base(self):
        primes = [2, 3, 5, 7]
        b = Base(8051, primes, 1)
        assert b.x_sq_minus_n_exp == [[0, 0, 0, 2]]
        assert b.x == [90]

        b = Base(8051, primes, 3)
        assert [0, 0, 0, 2] in b.x_sq_minus_n_exp
        assert len(b.x_sq_minus_n_exp) == 3
