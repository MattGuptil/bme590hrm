from makeJson import makej
import pytest
import json
import numpy as np


@pytest.mark.parametrize('myin, myin2, myin3, expect', [

    ({"key1": 'WOW', "key2": 'GEEZE'}, 'myTest.csv', 'myTest.json',
     {"key1": 'WOW', "key2": 'GEEZE'}),
    ({"key1": [1, 2, 3], "key2": 1}, 'myTest.csv', 'myTest.json',
     {"key1": [1, 2, 3], "key2": 1}),
    ({}, 'myTest.csv', 'myTest.json', {}),

])
def test_json(myin, myin2, myin3, expect):
    makej(myin, myin2)

    with open(myin3, 'r') as f:
        mydic = json.load(f)

    assert mydic == expect


@pytest.mark.parametrize('myin_, myin2_, expect_', [

    (1, 'myTest.csv', True),
    ({"key1": [1, 2, 3], "key2": 1}, 1, True),
    ({"key1": [1, 2, 3], "key2": 1}, 'myTest.csv', False),
    ({"key1": np.array([1, 2, 3])}, 'myTest.csv', True),
    (1, 1, True),
])
def test_json2(myin_, myin2_, expect_):
    try:
        makej(myin_, myin2_)
        myb = False
    except TypeError:
        myb = True
    finally:
        assert myb == expect_
