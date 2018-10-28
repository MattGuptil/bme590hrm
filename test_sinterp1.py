from sinterp import *
import pytest
import numpy as np


@pytest.mark.parametrize('myi, expec', [

    (np.array([-999, 1, -999, -999, 5, 7, -999, 15, -999]),
     np.array([0, 1, 2, 3, 5, 7, 9, 15, 0])),
    (np.array([-999, -999, -999, -999, -999, -999, -999, -999, -999]),
     np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])),

])
def test_sinterp(myi, expec):
    t = sinterp1(myi)

    try:
        np.testing.assert_equal(t, expec)
    except AssertionError:
        assert False


@pytest.mark.parametrize('myi_, expec_', [

    (np.array([-999, 1, -999, -999, 5, 7, -999, 15, -999]),
     False),
    (np.array([-999, -999, -999, -999, -999, -999, -999, -999, -999]),
     False),
    (np.array([]), True),
    ([], True),
    (1, True),
    ('', True),
    ('sdfd', True),

])
def test_sinterp2(myi_, expec_):
    try:
        sinterp1(myi_)
        myb = False
    except TypeError:
        myb = True
    finally:
        assert myb == expec_
