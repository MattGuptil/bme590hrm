import Datacollector
import pytest
import numpy as np


@pytest.mark.parametrize('myin, expect1', [

    ('\\collector_test1.csv', True),
    ('\\test_data100.csv', True),
    ('\\test_data.csv', True),
    ('', True),
    ([], True),
    (1, True),
    (np.array([]), True),


])
def test_collector(myin, expect1):
    Datacollector.input = lambda __: myin

    try:
        Datacollector.collector()
        myb = False
    except FileNotFoundError:
        myb = True
    except IOError:
        myb = True
    except TypeError:
        myb = True
    finally:
        assert myb == expect1
