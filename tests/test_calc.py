import pytest
from calc import line, square, cube


@pytest.mark.parametrize('a, b, answer', [
    (1, 2, [-2.0]),
    (1, -3, [3.0]),
    (1, 'Masha', [])
])
def test_calcline(a, b, answer):
    assert line(a, b) == answer


@pytest.mark.parametrize('a, b, c, answer', [
    (1, -3, -4, [4, -1]),
    (2, 4, 2, [4, -1])

])
def test_calcSquare(a, b, c, answer):
    assert square(a, b, c) == answer


@pytest.mark.parametrize('a, b, c, d, answer', [(1, -5, 8, -4, [1.0, 2.0, 2.0])])
def test_calcCube(a, b, c, d, answer):
    assert cube(a, b, c, d) == answer


def test_lineNegative(human):
    assert line() == []
