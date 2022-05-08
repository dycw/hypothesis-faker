from decimal import Decimal
from typing import Any
from typing import Callable

from hypothesis import given
from hypothesis.strategies import DataObject
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import data
from pytest import mark
from pytest import param

from hypothesis_faker import abas
from hypothesis_faker import addresses
from hypothesis_faker import bank_countries
from hypothesis_faker import bbans
from hypothesis_faker import building_numbers
from hypothesis_faker import cities
from hypothesis_faker import city_suffixes
from hypothesis_faker import coordinates
from hypothesis_faker import countries
from hypothesis_faker import country_codes
from hypothesis_faker import current_countries
from hypothesis_faker import current_country_codes
from hypothesis_faker import ibans
from hypothesis_faker import license_plates
from hypothesis_faker import postcodes
from hypothesis_faker import street_addresses
from hypothesis_faker import street_names
from hypothesis_faker import street_suffixes
from hypothesis_faker import swift8s
from hypothesis_faker import swift11s
from hypothesis_faker import swifts
from tests.utilities import env


@given(data=data())
@mark.parametrize(
    ["strategy", "type"],
    [
        # address #############################################################
        param(addresses, str),
        param(building_numbers, str),
        param(cities, str),
        param(city_suffixes, str),
        param(countries, str),
        param(country_codes, str),
        param(current_countries, str),
        param(current_country_codes, str),
        param(postcodes, str),
        param(street_addresses, str),
        param(street_names, str),
        param(street_suffixes, str),
        # automotive ##########################################################
        param(license_plates, str),
        # bank ################################################################
        param(abas, str),
        param(bank_countries, str),
        param(bbans, str),
        param(ibans, str),
        param(swifts, str),
        param(swift11s, str),
        param(swift8s, str),
        # geo #################################################################
        param(coordinates, Decimal),
    ],
)
def test_strategies(
    data: DataObject, strategy: Callable[..., SearchStrategy[Any]], type: type
) -> None:
    with env():
        assert isinstance(data.draw(strategy()), type)
