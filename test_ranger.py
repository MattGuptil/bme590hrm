from sinterp import ranger
import pytest


@pytest.mark.parametrize('myin, expect', [

    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([1, 350, 200], [1, 299, 200]),
    ([-1, -350, 200], [-1, -299, 200]),

])
def test_ranger(myin, expect):
    v = ranger(myin)

    assert v == expect
