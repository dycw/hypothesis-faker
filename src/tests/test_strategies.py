from decimal import Decimal
from typing import Any
from typing import Callable

from hypothesis import given
from hypothesis.strategies import DataObject
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import data
from pytest import mark
from pytest import param

from hypothesis_faker import addresses
from hypothesis_faker import building_numbers
from hypothesis_faker import coordinates
from tests.utilities import env


@given(data=data())
@mark.parametrize(
    ["strategy", "type"],
    [
        # address #############################################################
        param(addresses, str),
        param(building_numbers, str),
        # geo #################################################################
        param(coordinates, Decimal),
    ],
)
def test_strategies(
    data: DataObject, strategy: Callable[..., SearchStrategy[Any]], type: type
) -> None:
    with env():
        assert isinstance(data.draw(strategy()), type)
