from main import get_min_number


def test_func_returns_expected_integer():
    v = [-7, -1, 8, 7, 9, -9]
    assert get_min_number(v) == 7, get_min_number(v)

