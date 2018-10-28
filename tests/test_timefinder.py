from newindice import timefinder
import pytest
import numpy as np


@pytest.mark.parametrize('myin, myin2, expect', [

    (np.array([1, 2, 3]), np.array([0, 2]), np.array([1, 3])),

])
def test_timefinder(myin, myin2, expect):
    nt = timefinder(myin, myin2)
    try:
        np.testing.assert_equal(nt, expect)
    except AssertionError:
        assert False


@pytest.mark.parametrize('myin_, myin2_, expect_', [

    (np.array([1, 2, 3]), np.array([0, 2]), False),
    (np.array([]), np.array([0, 2]), True),
    (np.array([1, 2, 3]), np.array([]), True),
    ([], np.array([0, 2]), True),
    (np.array([1, 2, 3]), [], True),
    ([], [], True),
    ([1], [1, 2], True)

])
def test_timefinder2(myin_, myin2_, expect_):
    try:
        timefinder(myin_, myin2_)
        myb = False
    except TypeError:
        myb = True
    except ValueError:
        myb = True
    finally:
        assert myb == expect_
