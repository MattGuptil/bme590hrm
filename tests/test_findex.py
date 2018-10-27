from newindice import findex
import pytest
import numpy as np


@pytest.mark.parametrize('myin, expect', [

    (np.array([1, 2, 3]), [3, 1]),
    (([1, 2, 3]), [3, 1]),
    (np.array([3, -2, 1]), [3, -2]),

])
def test_json(myin, expect):
    nt, mt = findex(myin)

    assert nt == expect[0]
    assert mt == expect[1]