from hypothesis import given
from hypothesis.strategies import integers


@given(integers(min_value=0, max_value=10000))
def test_sum_range(n):
    assert n*(n+1) / 2 == sum(range(n + 1))
