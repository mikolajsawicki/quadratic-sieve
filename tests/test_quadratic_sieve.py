from quadratic_sieve.quadratic_sieve import *
from unittest import TestCase


class TestQuadraticSieve(TestCase):

    def test_value(self):
        assert value([2, 0, 3], [3, 5, 7]) == 3087

    def test_qs(self):
        assert factorize(1649, base_size=3) == (17, 97)
        assert factorize(8051, base_size=3) == (83, 97)
        assert factorize(112, base_size=1) == (8, 14)
