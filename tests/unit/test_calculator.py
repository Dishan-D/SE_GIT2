import pytest
from src.calculator import add, subtract, multiply, divide, power, square_root

class TestBasicOperations:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5
        assert add(10, 15) == 25

    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

class TestMultiplyDivideWithValidation:
    def test_multiply_input_validation(self):
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")

    def test_divide_input_validation(self):
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

class TestAdvancedOperations:
    def test_power_positive_numbers(self):
        assert power(2, 3) == 8
        assert power(5, 2) == 25

    def test_power_zero_exponent(self):
        assert power(5, 0) == 1
        assert power(0, 0) == 1

    def test_square_root_positive_numbers(self):
        assert square_root(4) == 2
        assert square_root(9) == 3
        assert square_root(16) == 4

    def test_square_root_negative_raises_error(self):
        with pytest.raises(ValueError, match="Cannot calculate square root of negative"):
            square_root(-4)