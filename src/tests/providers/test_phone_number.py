from __future__ import annotations

from hypothesis import given
from hypothesis.strategies import DataObject
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import data
from pytest import mark

from hypothesis_faker.providers.phone_number import country_calling_codes
from hypothesis_faker.providers.phone_number import msisdns
from hypothesis_faker.providers.phone_number import phone_numbers


@mark.parametrize("strategy", [country_calling_codes, msisdns, phone_numbers])
@given(data=data())
def test_color_strategies(
    data: DataObject, strategy: SearchStrategy[str]
) -> None:
    assert isinstance(data.draw(strategy), str)
