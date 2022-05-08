from hypothesis import given

from hypothesis_faker import addresses


@given(address=addresses())
def test_addresses(address: str) -> None:
    assert isinstance(address, str)
