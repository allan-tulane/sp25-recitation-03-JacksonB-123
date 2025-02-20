from main import *


## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3 * 3
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(1)) == 1 * 1
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(2)) == 1 * 2
    assert quadratic_multiply(BinaryNumber(7), BinaryNumber(6)) == 7 * 6
    quadratic_multiply_time(2, 2, quadratic_multiply) == 2 * 2
    quadratic_multiply_time(3, 2, quadratic_multiply) == 3 * 2
    quadratic_multiply_time(4, 6, quadratic_multiply) == 4 * 6
    quadratic_multiply_time(5, 7, quadratic_multiply) == 5 * 7
    quadratic_multiply_time(9, 1, quadratic_multiply) == 9 * 1
