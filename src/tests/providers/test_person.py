from __future__ import annotations

from hypothesis import given
from hypothesis.strategies import DataObject
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import data
from pytest import mark

from hypothesis_faker.providers.person import first_names
from hypothesis_faker.providers.person import first_names_female
from hypothesis_faker.providers.person import first_names_male
from hypothesis_faker.providers.person import first_names_nonbinary
from hypothesis_faker.providers.person import language_names
from hypothesis_faker.providers.person import last_names
from hypothesis_faker.providers.person import last_names_female
from hypothesis_faker.providers.person import last_names_male
from hypothesis_faker.providers.person import last_names_nonbinary
from hypothesis_faker.providers.person import names
from hypothesis_faker.providers.person import names_female
from hypothesis_faker.providers.person import names_male
from hypothesis_faker.providers.person import names_nonbinary
from hypothesis_faker.providers.person import prefixes
from hypothesis_faker.providers.person import prefixes_female
from hypothesis_faker.providers.person import prefixes_male
from hypothesis_faker.providers.person import prefixes_nonbinary
from hypothesis_faker.providers.person import suffixes
from hypothesis_faker.providers.person import suffixes_female
from hypothesis_faker.providers.person import suffixes_male
from hypothesis_faker.providers.person import suffixes_nonbinary


@given(data=data())
@mark.parametrize(
    "strategy",
    [
        first_names,
        first_names_female,
        first_names_male,
        first_names_nonbinary,
        language_names,
        last_names,
        last_names_female,
        last_names_male,
        last_names_nonbinary,
        names,
        names_female,
        names_male,
        names_nonbinary,
        prefixes,
        prefixes_male,
        prefixes_female,
        prefixes_nonbinary,
        suffixes,
        suffixes_female,
        suffixes_male,
        suffixes_nonbinary,
    ],
)
def test_person_strategies(
    data: DataObject, strategy: SearchStrategy[str]
) -> None:
    assert isinstance(data.draw(strategy), str)
