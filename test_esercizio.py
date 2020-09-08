from main import get_min_number, MIN_VALUE, MAX_VALUE, InvalidValue
from nose.tools import assert_raises, assert_raises_regexp


def test_func_returns_expected_integer():
    v = [-7, -1, 8, 7, 9, -9]
    assert get_min_number(v) == 7, get_min_number(v)
    v = [2, 2, 4, -2, 4, -2]
    assert get_min_number(v) == 2, get_min_number(v)
    v = [8, 3, -3, 9, -8]
    assert get_min_number(v) == 3, get_min_number(v)


def test_func_returns_zero_if_opposite_integer_not_present():
    v = [-1, -3, -4, 5, 7, 2]
    assert get_min_number(v) == 0, get_min_number(v)


def test_func_raises_error_if_list_member_not_between_threesholds():
    assert_raises(
        InvalidValue,
        get_min_number,
        [MAX_VALUE + 1, 1, -89, -1]
    )

    assert_raises_regexp(
        InvalidValue,
        f'''Value "{MIN_VALUE - 1}" at position\
 3 is not an integer between 100000 and -100000''',
        get_min_number,
        [-1, 89, 1, MIN_VALUE - 1]
    )


def test_func_raises_error_if_list_member_is_not_an_int():
    assert_raises_regexp(
        InvalidValue,
        f'''Value "NOT AN INTEGER" at position\
 3 is not an integer between 100000 and -100000''',
        get_min_number,
        [-1, 89, 1, 'NOT AN INTEGER']
    )

    assert_raises_regexp(
        InvalidValue,
        f'''Value "5.0" at position\
 3 is not an integer between 100000 and -100000''',
        get_min_number,
        [-1, 89, 1, 5.0]
    )
