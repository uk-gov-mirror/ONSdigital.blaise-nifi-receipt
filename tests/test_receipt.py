from receipt import is_errored


def test_is_errored_true():
    assert is_errored({"errorOutput": "foobar"}) is True


def test_is_errored_false():
    assert is_errored({"anything": "foobar"}) is False
