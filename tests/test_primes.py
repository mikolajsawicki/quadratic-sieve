from quadratic_sieve.primes import *
from unittest import TestCase


class TestPrimes(TestCase):

    def test_legendre(self):
        probes = [
            [64, 3, 1],
            [65, 3, -1],
            [66, 3, 0],
            [66, 9, 0],
        ]

        for n, p, leg in probes:
            assert legendre(n, p) == leg, 'legendre(%s, %s) should be %s' % (n, p, leg)

        assert [p for p in get_smooth_primes(23)[1:] if legendre(8051, p) == 1] == [5, 7, 13, 23]

    def test_load_primes(self):
        assert get_smooth_primes(23) == [2, 3, 5, 7, 11, 13, 17, 19, 23]

    def test_factorize(self):
        assert factorize(12, [2, 3, 5, 7]) == [2, 1, 0, 0]
        assert factorize(24, [2, 3, 5, 7, 11]) == [3, 1, 0, 0, 0]
        assert factorize(49, [2, 3, 5, 7]) == [0, 0, 0, 2]
