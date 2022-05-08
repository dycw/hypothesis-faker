from hypothesis import given
from hypothesis.strategies import DataObject
from hypothesis.strategies import data

from hypothesis_faker import addresses
from tests.utilities import env


@given(data=data())
def test_addresses(data: DataObject) -> None:
    with env():
        assert isinstance(data.draw(addresses()), str)
