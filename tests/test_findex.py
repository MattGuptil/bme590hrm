from newindice import findex
import pytest
import numpy as np


@pytest.mark.parametrize('myin, expect', [

    (np.array([1, 2, 3]), [3, 1]),
    (([1, 2, 3]), [3, 1]),
    (np.array([3, -2, 1]), [3, -2]),

])
def test_findex(myin, expect):
    nt, mt = findex(myin)

    assert nt == expect[0]
    assert mt == expect[1]


@pytest.mark.parametrize('myin_, expect_', [

    (np.array([1, 2, 3]), False),
    (([1, 2, 3]), False),
    (np.array([3, -2, 1]), False),
    ([], True),
    (1, True),
    ('n', True),


])
def test_findex2(myin_, expect_):
    try:
        findex(myin_)
        myb = False
    except TypeError:
        myb = True
    finally:
        assert myb == expect_
