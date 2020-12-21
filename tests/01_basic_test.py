#!/usr/bin/python
# -*- coding: latin-1 -*-
import time
from other_code.services import DATA_SET_A, DATA_SET_B, DATA_SET_C


def test_example():
    print("\nRunning basic test1... before pause")
    time.sleep(25)
    print("\nRunning basic test1... after pause")
    assert 1 == 2
    
def test_example():
    print("\nRunning basic test2... before pause")
    time.sleep(25)
    print("\nRunning basic test2... after pause")
    assert 1 == 2
