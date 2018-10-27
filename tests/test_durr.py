from newindice import durr
import pytest
import numpy as np


@pytest.mark.parametrize('myin, expect', [

    (np.array([1, 2, 3]), 2),
    (([1, 2, 3]), 2),
    (np.array([3, 2, 1]), -2),

])
def test_json(myin, expect):
    nt = durr(myin)

    assert nt == expect
    # try:
    #     np.testing.assert_equal(nt, expect)
    # except AssertionError:
    #     assert False
