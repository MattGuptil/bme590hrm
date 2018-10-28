from NotUsed.intervals import intervs
import pytest
import numpy as np


@pytest.mark.parametrize('myIn, myIn2, Expect', [

	([0, 1, 1.01, 2, 3, 3.01], [0, 1, 2, 3, 4, 5], [0, 1, 3, 4]),

])
def test_interval(myIn, myIn2, Expect):
	re = intervs(myIn, myIn2)

	try:
		np.testing.assert_array_equal(re, Expect, 'SIKE')
	except AssertionError:
		assert False
