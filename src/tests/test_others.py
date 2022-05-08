from tempfile import TemporaryDirectory

from hypothesis import given
from hypothesis.strategies import DataObject
from hypothesis.strategies import data
from tempenv import TemporaryEnvironment

from hypothesis_faker import addresses


@given(data=data())
def test_max_items(data: DataObject) -> None:
    with TemporaryDirectory() as temp_dir, TemporaryEnvironment(
        {"HYPOTHESIS_FAKER_ROOT": temp_dir, "HYPOTHESIS_FAKER_MAX_ITEMS": "10"}
    ):
        _ = data.draw(addresses())
