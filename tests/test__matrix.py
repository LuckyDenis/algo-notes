# coding: utf8
import pytest
from matrix import sum_diagonals
from matrix import transposed_mtx


@pytest.mark.matrix
@pytest.mark.parametrize("mtx, correct", [
    ([[1]], 1),
    ([[1, 1], [1, 1]], 4),
    ([[1, 2, 3], [1, 2, 3], [1, 2, 3]], 10),
    ([[-1, 2, 3], [1, 2, 3], [-1, 2, 3]], 6)
])
def test__sum_diagonals(mtx, correct):
    result = sum_diagonals(mtx)
    assert result == correct


@pytest.mark.matrix
@pytest.mark.parametrize("mtx, correct", [
    ([[1]], [[1]]),
    ([[1, 1], [2, 2]], [[1, 2], [1, 2]]),
    ([[1, 1], [2, 2], [3, 3]], [[1, 2, 3], [1, 2, 3]]),
    ([[1, 1, 1], [2, 2, 2]], [[1, 2], [1, 2], [1, 2]])
])
def test__transposed_mtx(mtx, correct):
    result = transposed_mtx(mtx)
    assert result == correct
