# tests/lib_test.py
from toolbox.haversine import haversine

def test_haversine():
    assert haversine(1,2,10,-20) > 0