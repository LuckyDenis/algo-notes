# coding: utf8
import pytest
import nums


@pytest.mark.numbers
@pytest.mark.parametrize("num, correct", [
        (21, [2, 3, 5, 7, 11, 13, 17, 19]),
        (2, [2]),
        (3, [2, 3]),
        (7, [2, 3, 5, 7]),
        (10, [2, 3, 5, 7])
     ])
def test__find_simple_numbers(num, correct):
    assert nums.simple_numbers(num) == correct


@pytest.mark.numbers
@pytest.mark.parametrize("num, correct", [
    (0, 1), (1, 1), (2, 2), (3, 6),
    (4, 24), (5, 120), (10, 3628800),
    (20, 2432902008176640000)
])
def test__factorial_tree(num, correct):
    assert nums.fact_tree(num) == correct


@pytest.mark.numbers
@pytest.mark.parametrize("num, correct", [
    (21, [3, 7]), (2, [1, 2]), (17, [1, 17]),
    (25, [5, 5]), (60, [2, 2, 3, 5])])
def test__factorize(num, correct):
    assert nums.factorize(num) == correct


@pytest.mark.numbers
@pytest.mark.parametrize("formula, answer", [
    ("-1+(1+2.76)*4.1 *pi +5!", 167.43079234774024),
    ("sin(3- 2)", 0.8414709848078965)
])
def test__reverse_polish_notation(formula, answer):
    assert nums.reverse_polish_notation(formula) == answer
