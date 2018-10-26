from makeJson import makej
import pytest
import json


@pytest.mark.parametrize('myin, myin2, myin3, expect', [

    ({"key1": 'WOW', "key2": 'GEEZE'}, 'myTest.csv', 'myTest.json', {"key1": 'WOW', "key2": 'GEEZE'}),
    ({"key1": [1, 2, 3], "key2": 1}, 'myTest.csv', 'myTest.json', {"key1": [1, 2, 3], "key2": 1}),


])
def test_json(myin, myin2, myin3, expect):
    makej(myin, myin2)

    with open(myin3, 'r') as f:
        mydic = json.load(f)

    assert mydic == expect
