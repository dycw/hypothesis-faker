from decimal import Decimal

from hypothesis import given
from hypothesis.strategies import DataObject
from hypothesis.strategies import data

from hypothesis_faker import addresses
from hypothesis_faker.strategies import coordinates
from tests.utilities import env


@given(data=data())
def test_addresses(data: DataObject) -> None:
    with env():
        assert isinstance(data.draw(addresses()), str)


@given(data=data())
def test_coordinates(data: DataObject) -> None:
    with env():
        assert isinstance(data.draw(coordinates()), Decimal)
