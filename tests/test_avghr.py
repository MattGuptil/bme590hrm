import newindice
import pytest
import numpy as np
#  from unittest.mock import patch


@pytest.mark.parametrize('myin, myin2, expect', [

    (4, np.array([1, 2, 3, 4]), 60),


])
#  @patch('builtins.input', side_effect=["1"])
def test_avghr(myin, myin2, expect):
    newindice.input = lambda _: "1"
    nt = newindice.avghr(myin, myin2)

    assert nt == expect


@pytest.mark.parametrize('myin_, myin2_, expect_', [

    (4, np.array([1, 2, 3, 4]), False),
    ('myst', np.array([1, 2, 3, 4]), True),
    (3, np.array([]), True),
    ('myst', np.array([]), True),
    (float('Nan'), np.array([1, 2, 3, 4]), True),
    (4, 5, True),
    (3, 'g', True),
    (np.float(3), np.array([1, 2, 3, 4]), False),


])
def test_avhr2(myin_, myin2_, expect_):
    newindice.input = lambda _: "1"
    try:
        newindice.avghr(myin_, myin2_)
        myb2 = False
    except TypeError:
        myb2 = True
    finally:
        assert myb2 == expect_
