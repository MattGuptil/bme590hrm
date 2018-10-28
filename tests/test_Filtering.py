from Filtering import myfilter
import pytest
import numpy as np


@pytest.mark.parametrize('myin1, expect1, expect2', [

    ([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
     [1.06899629, 2.04843588, 3.01509552, 3.97452878, 4.93318819,
      5.89789906, 6.8752924, 7.87120641, 8.89007248, 9.93431046,
      11.00376906, 11.09525773, 13.20222534, 14.31464498, 15.41916182,
      16.49954989]),

])
def test_filtering(myin1, expect1, expect2):
    v = myfilter(myin1)
    print(v[1])
    assert np.array_equal(v[0], expect1)
    assert not np.array_equal(v[1], expect2)


@pytest.mark.parametrize('myin_, expect_', [

    ([1, 2, 3, 4], True),
    ([1, 350, 200], True),
    ([-1, -350, 200], True),
    ([], True),
    (np.array([]), True),
    (1, True),
    ('tt', True),
    ('', True),
    ([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]], False),

])
def test_filtering2(myin_, expect_):
    try:
        myfilter(myin_)
        myb = False
    except TypeError:
        myb = True
    finally:
        assert myb == expect_
