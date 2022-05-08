from decimal import Decimal
from typing import Optional
from typing import Union

from hypothesis.strategies import SearchStrategy

from hypothesis_faker.providers import Provider


# address #####################################################################


def addresses() -> SearchStrategy[str]:
    return Provider.address.get_strategy()


def building_numbers() -> SearchStrategy[str]:
    return Provider.building_number.get_strategy()


def cities() -> SearchStrategy[str]:
    return Provider.city.get_strategy()


def city_suffixes() -> SearchStrategy[str]:
    return Provider.city_suffix.get_strategy()


def countries() -> SearchStrategy[str]:
    return Provider.country.get_strategy()


def country_codes(*, representation: str = "alpha-2") -> SearchStrategy[str]:
    return Provider.country_code.get_strategy(representation=representation)


def current_countries() -> SearchStrategy[str]:
    return Provider.current_country.get_strategy()


def current_country_codes() -> SearchStrategy[str]:
    return Provider.current_country_code.get_strategy()


def postcodes() -> SearchStrategy[str]:
    return Provider.postcode.get_strategy()


def street_addresses() -> SearchStrategy[str]:
    return Provider.street_address.get_strategy()


def street_names() -> SearchStrategy[str]:
    return Provider.street_name.get_strategy()


def street_suffixes() -> SearchStrategy[str]:
    return Provider.street_suffix.get_strategy()


# geo #########################################################################


def coordinates(
    *, center: Optional[float] = None, radius: Union[float, int] = 0.001
) -> SearchStrategy[Decimal]:
    return Provider.coordinate.get_strategy(center=center, radius=radius)
