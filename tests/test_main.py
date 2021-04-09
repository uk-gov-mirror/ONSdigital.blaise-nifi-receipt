import base64

from main import load_receipt


def test_load_receipt():
    event = {"data": base64.b64encode(b'{"key": "value"}')}
    assert load_receipt(event) == {"key": "value"}
