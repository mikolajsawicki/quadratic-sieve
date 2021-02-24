import copy
from math import ceil
from .primes import factorize


class Base:

    def __init__(self, n, primes, base_size):
        self.n = n
        self.width = len(primes)
        self.size = base_size
        self.primes = copy.deepcopy(primes)
        self.x = []
        self.x_sq_minus_n = []
        self.x_sq_minus_n_exp = []

        self.generate()

    def generate(self):
        x = ceil(self.n ** 0.5)

        i = 0

        while i < self.size:
            t = x ** 2 - self.n
            t_exp = factorize(t, self.primes)

            if t_exp is not None:
                i += 1
                self.x.append(x)
                self.x_sq_minus_n.append(t)
                self.x_sq_minus_n_exp.append(t_exp)

            x += 1
