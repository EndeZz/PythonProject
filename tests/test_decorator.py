import pytest
from decorator import pow, square


@pytest.mark.parametrize('a, b, c, answer', [
    (4, 3, 1, 16),
    (3, 2, 3, -1)
])
def test_power(a, b, c, answer):
    @pow(power=a)
    def f3(x, y):
        return x - y
    assert f3(b, c) == answer


@pytest.mark.parametrize('a, b, answer', [(2, 2, 16)])
def test_square(a, b, answer):
    @square
    def f2(x, y):
        return x * y
    assert f2(a, b) == answer
