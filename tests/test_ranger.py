from sinterp import *
import pytest


@pytest.mark.parametrize('myin, expect', [

    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([1, 350, 200], [1, 299, 200]),
    ([-1, -350, 200], [-1, -299, 200]),
    (np.array([-1, -350, 200]), np.array([-1, -299, 200])),

])
def test_ranger(myin, expect):
    v = ranger(myin)

    assert np.array_equal(v, expect)


@pytest.mark.parametrize('myin_, expect_', [

    ([1, 2, 3, 4], False),
    ([1, 350, 200], False),
    ([-1, -350, 200], False),
    ([], True),
    (np.array([]), True),
    (1, True),
    ('tt', True),
    ('', True)

])
def test_ranger2(myin_, expect_):
    try:
        ranger(myin_)
        myb = False
    except TypeError:
        myb = True
    finally:
        assert myb == expect_
