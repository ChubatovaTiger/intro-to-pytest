import pytest


def checkconfig(x):
    pytest.fail("not configured:")


def test_something():
    checkconfig(42)
