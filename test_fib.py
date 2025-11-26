import pytest
from fib import fib_sum

@pytest.mark.parametrize("n, expected_sum", [
    (0, 0),
    (1, 0),
    (2, 1),
    (5, 7),
    (10, 88),
])
def test_fib_sum(n, expected_sum):
    assert fib_sum(n) == expected_sum