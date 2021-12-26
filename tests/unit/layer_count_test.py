from serverless_project.count import Adder, Multiplier


def test_adder__add():
    subject = Adder()
    assert subject.add(2, 2) == 4


def test_multiplier__multiply():
    subject = Multiplier()
    assert subject.multiply(3, 3) == 9
