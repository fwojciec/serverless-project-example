from serverless_project.count import Math


def test_math__add():
    subject = Math()
    assert subject.add(2, 2) == 4


def test_math__multiply():
    subject = Math()
    assert subject.multiply(3, 3) == 9
