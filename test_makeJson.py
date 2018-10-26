from makeJson import makeJ
import pytest
import numpy as np
import json

@pytest.mark.parametrize('myIn, myIn2, myIn3, Expect', [

	({"key1": 'WOW',"key2": 'GEEZE'},'myTest.csv','myTest.json', {"key1": 'WOW',"key2": 'GEEZE'}),
	

	])


def test_jSon(myIn,myIn2,myIn3,Expect):
	makeJ(myIn,myIn2)

	with open(myIn3, 'r') as f:
		mydic = json.load(f)

	assert mydic == Expect

