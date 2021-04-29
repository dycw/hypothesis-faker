from hypothesis import given
from hypothesis import settings
from hypothesis.strategies import DataObject
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import data
from pytest import mark

from hypothesis_faker.providers.person import first_names_female
from hypothesis_faker.providers.person import first_names_male
from hypothesis_faker.providers.person import last_names
from hypothesis_faker.providers.person import names
from hypothesis_faker.providers.person import prefixes_female
from hypothesis_faker.providers.person import prefixes_male
from hypothesis_faker.providers.person import suffixes_female
from hypothesis_faker.providers.person import suffixes_male


@given(data=data())
@settings(max_examples=1000)
@mark.parametrize(
    "strategy",
    [
        first_names_female,
        first_names_male,
        last_names,
        names,
        prefixes_male,
        prefixes_female,
        suffixes_female,
        suffixes_male,
    ],
)
def test_person_strategies(
    data: DataObject, strategy: SearchStrategy[str]
) -> None:
    assert isinstance(data.draw(strategy), str)
