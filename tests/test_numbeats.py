from newindice import numbeats
import pytest
import numpy as np


@pytest.mark.parametrize('myin, expect', [

    (np.array([1, 2, 3]), 3),
    ([1, 2, 3], 3),

])
def test_numbeats(myin, expect):
    nt = numbeats(myin)

    assert nt == expect


@pytest.mark.parametrize('myin_, expect_', [

    (np.array([1, 2, 3]), False),
    (np.array([]), True),
    ([], True),
    (1, True),
    ('df', True),

])
def test_numbeats2(myin_, expect_):
    try:
        numbeats(myin_)
        myb = False
    except TypeError:
        myb = True
    finally:
        assert myb == expect_
