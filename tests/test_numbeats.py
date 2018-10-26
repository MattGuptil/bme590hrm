from newindice import numbeats
import pytest
import numpy as np


@pytest.mark.parametrize('myin, expect', [

    (np.array([1, 2, 3]), 3),


])
def test_json(myin, expect):
    nt = numbeats(myin)

    assert nt == expect
