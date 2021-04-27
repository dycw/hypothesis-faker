from faker import Faker
from hypothesis import given
from hypothesis import settings
from pytest import mark

from hypothesis_faker.providers.person import names


@given(name=names)
def test_names(name: str) -> None:
    assert isinstance(name, str)


@mark.skip
@given(name=names)
@settings(derandomize=True)
def test_names_example(name: str) -> None:
    f = Faker()
    f.name()
    assert name == "asdf"
