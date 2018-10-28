from newindice import durr
import pytest
import numpy as np


@pytest.mark.parametrize('myin, expect', [

    (np.array([1, 2, 3]), 2),
    (([1, 2, 3]), 2),
    (np.array([3, 2, 1]), -2),
    (np.array([-3, 2, 1]), 4)

])
def test_durr(myin, expect):
    nt = durr(myin)

    assert nt == expect
    # try:
    #     np.testing.assert_equal(nt, expect)
    # except AssertionError:
    #     assert False


@pytest.mark.parametrize('myin_, expect_', [

    (np.array([1, 2, 3]), False),
    (([1, 2, 3]), False),
    ([], True),
    (1, True),
    ('my', True),

])
def test_durr2(myin_, expect_):
    try:
        durr(myin_)
        myb = False
    except TypeError:
        myb = True
    finally:
        assert myb == expect_
