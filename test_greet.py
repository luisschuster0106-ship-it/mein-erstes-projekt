from greet import greet


def test_greet_default():
    assert greet() == "Hallo, Welt!"


def test_greet_with_name():
    assert greet("Anja") == "Hallo, Anja!"
