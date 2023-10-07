import pytest
import numpy.testing as npt
from example_functions import my_adder, my_thermo_stat, have_digits


# Tests for my_adder
@pytest.mark.parametrize(
    ["number_1", "number_2", "number_3", "expected_result"],
    [
        (1, 2, 3, 6),
        (-5, -10, 17, 2),
        (13.1, 22.4, 52.1, 87.6),
    ],
)
def test_my_adder(number_1, number_2, number_3, expected_result):
    final_result = my_adder(number_1, number_2, number_3)
    npt.assert_almost_equal(final_result, expected_result)


# Tests for have_digits
@pytest.mark.parametrize(
    ["input_string", "expected_result"],
    [
        ("aa2ss41d.dd2", 1),
        ("%$%jkalnslf((lanflanlfn))", 0),
        ("Quantum_Chemistry, not cool at all!!!", 0),
    ],
)
def test_have_digits(input_string, expected_result):
    final_result = have_digits(input_string)
    npt.assert_almost_equal(final_result, expected_result)


# Tests for my_thermo_stat
def test_thermo_heat():
    assert my_thermo_stat(10, 25) == "Heat"


def test_thermo_cool():
    assert my_thermo_stat(31, 25) == "AC"


def test_thermo_fine():
    assert my_thermo_stat(24, 25) == "off"
