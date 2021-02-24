from quadratic_sieve.fast_gauss import *
from unittest import TestCase


class TestFastGauss(TestCase):

    def test_gf2(self):
        assert gf2([
            [1, 1, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 1, 1],
            [2, 0, 1, 0],
            [0, 2, 0, 1]
        ]) == [
                   [1, 1, 0, 0],
                   [1, 1, 0, 1],
                   [0, 1, 1, 1],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]
               ]

    def test_fast_gauss(self):
        assert fast_gauss([
            [1, 1, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 1, 1],
            [2, 0, 1, 0],
            [0, 2, 0, 1]
        ]) == ([
                   [1, 0, 0, 0],
                   [0, 0, 0, 1],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [1, 0, 0, 1]
               ], [True, True, True, True, False])

    def test_perfect_square_combinations(self):
        assert [i for i in perfect_square_combinations([
            [1, 1, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 1, 1],
            [2, 0, 1, 0],
            [0, 2, 0, 1]
        ])] == [[0, 1, 4]]
