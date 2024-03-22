import sys
import pytest


def squared(n: float) -> float:
    return n ** 2


def unit_test_squared():
    zero_squared = squared(0)
    one_squared = squared(1)
    two_squared = squared(2)
    m_one_squared = squared(-1)
    m_two_squared = squared(-2)

    tests = {
        "zero_squared": (zero_squared, 0),
        "one_squared": (one_squared, 1),
        "two_squared": (two_squared, 4),
        "m_one_squared": (m_one_squared, 1),
        "m_two_squared": (m_two_squared, 4),
        "a_wrong_test": (zero_squared, 999),
    }


    for test_name, (val, correct_value) in tests.items():
        if (val == correct_value):
            print(f"{test_name}: success - {val} = {correct_value}")
        else:
            print(f"{test_name}: failure - {val} != {correct_value}")

if sys.argv[1] == "TEST":
    unit_test_squared()
