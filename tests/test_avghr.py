import newindice
import pytest
import numpy as np
from unittest.mock import patch


@pytest.mark.parametrize('myin, myin2, expect', [

    (4, np.array([1, 2, 3, 4]), 60),


])
#  @patch('builtins.input', side_effect=["1"])
def test_avghr(myin, myin2, expect):
    newindice.input = lambda _: "1"
    nt = newindice.avghr(myin, myin2)

    assert nt == expect
