from shared.math import Addition, Multiplication


def test_math_addition__add():
    subject = Addition()
    assert subject.add(2, 2) == 4


def test_math_multiplication__multiply():
    subject = Multiplication()
    assert subject.multiply(3, 3) == 9
