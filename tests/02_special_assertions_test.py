import pytest
import time


def test_div_zero_exception():
    """
    pytest.raises can assert that exceptions are raised (catching them)
    """
    with pytest.raises(ZeroDivisionError):
        x = 1 / 0
        print("1/0 = {}".format(x))
        print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')


def test_keyerror_details():
    """
    The raised exception can be referenced, and further inspected (or asserted)
    """
    my_map = {"foo": "bar"}

    with pytest.raises(KeyError) as ke:
        baz = my_map["baz"]
        print("Found Baz: {}".format(baz))

    print("\n(Raised: {})".format(ke))
    print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')


def test_approximate_matches():
    """
    pytest.approx can be used to assert "approximate" numerical equality
    (compare UnitTest's "assertAlmostEqual")

    print("special_assertions_test before pause")
    time.sleep(60)
    print("special_assertions_test after pause")
    """
    assert (0.1 + 0.2) == pytest.approx(0.3)
