from sinterp import *
import pytest
import numpy as np


@pytest.mark.parametrize('myi, expec', [

    (np.array([-999, 1, -999, -999, 5, 7, -999, 15, -999]),
     np.array([0, 1, 2, 3, 5, 7, 9, 15, 0])),

])
def test_sinterp(myi, expec):
    t = sinterp1(myi)

    try:
        np.testing.assert_equal(t, expec)
    except AssertionError:
        assert False
