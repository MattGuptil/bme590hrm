from newindice import timefinder
import pytest
import numpy as np

@pytest.mark.parametrize('myin, myin2, expect', [

    (np.array([1, 2, 3]), np.array([0, 2]), np.array([1, 3])),

])
def test_json(myin, myin2, expect):
    nt = timefinder(myin, myin2)
    try:
        np.testing.assert_equal(nt, expect)
    except AssertionError:
        assert False
