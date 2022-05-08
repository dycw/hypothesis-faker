from hypothesis import given
from hypothesis.strategies import DataObject
from hypothesis.strategies import data
from hypothesis.strategies import integers

from hypothesis_faker import addresses
from hypothesis_faker.providers import Provider
from hypothesis_faker.settings import HYPOTHESIS_FAKER_MAX_ITEMS
from hypothesis_faker.settings import HYPOTHESIS_FAKER_UPDATE_FREQ
from tests.utilities import env


@given(data=data(), max_items=integers(1, 100))
def test_max_items(data: DataObject, max_items: int) -> None:
    with env({HYPOTHESIS_FAKER_MAX_ITEMS: str(max_items)}):
        _ = data.draw(addresses())
        assert len(Provider.address.get_items()) <= max_items


@given(data=data())
def test_load_items(data: DataObject) -> None:
    with env({HYPOTHESIS_FAKER_UPDATE_FREQ: "100"}):
        _ = data.draw(addresses())
        from hypothesis_faker.providers import _ITEMS  # type: ignore

        _ITEMS.clear()
        _ = data.draw(addresses())
