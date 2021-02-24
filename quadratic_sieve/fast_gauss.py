from numpy import array, where
from typing import Sequence, List, Tuple


def gf2(matrix: Sequence[Sequence[int]]) -> List[List[int]]:
    """Returns GF(2) form of matrix (only binary elements).

    :param matrix: matrix
    :return: matrix over GF(2)
    """
    return [[x % 2 for x in row] for row in matrix]


def fast_gauss(matrix: Sequence[Sequence[int]]) -> Tuple[List[List[int]], List[bool]]:
    """Performs a fast Gaussian Elimination over GF(2) on matrix.

    :param matrix: matrix to triangularize
    :return: triangularized matrix of zeros and ones.
    """
    m = array(gf2(matrix))

    marked = [False] * len(m)

    for j, column in enumerate(m.T):
        try:
            pivot = where(column == 1)[0][0]
            marked[pivot] = True

            for k, col in enumerate(m.T):
                if k == j:
                    continue

                if col[pivot] == 1:
                    m[:, k] += m[:, j]
                    m[:, k] %= 2

        except (ValueError, IndexError):
            pass

    return m.tolist(), marked


def perfect_square_combinations(base: Sequence[Sequence[int]]) -> List[List[int]]:
    """Generator for finding all perfect squares possible to form using factors from base.

    :param base: list of lists of exponents
    :return: list of lists containing indexes of base elements to use to form a perfect square
    """
    m, marked = fast_gauss(base)

    rows_independent = [r for i, r in enumerate(m) if marked[i]]
    rows_dependent = [(i, row) for i, row in enumerate(m) if not marked[i]]

    for i, row in rows_dependent:
        ones_cols = [j for j, x in enumerate(row) if x == 1]

        rows_reducing = []

        for c in ones_cols:
            # Get a whole column in independent rows and search for 1
            r = [r[c] for r in rows_independent].index(1)
            rows_reducing.append(r)

        yield rows_reducing + [i]
