from typing import Callable

from faker.providers.person import Provider as PersonProvider
from faker.providers.person.en_US import Provider as PersonProviderEnUS
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import composite
from hypothesis.strategies import fixed_dictionaries
from hypothesis.strategies import sampled_from

from hypothesis_faker.types import T
from hypothesis_faker.utilities import PATTERN_FOR_DOUBLE_BRACES
from hypothesis_faker.utilities import WeightedList
from hypothesis_faker.utilities import fill_format_string
from hypothesis_faker.utilities import weighted_samples


_LANGUAGE_NAMES = PersonProvider.language_names
_FORMATS_MALE: WeightedList[str] = WeightedList(
    PersonProviderEnUS.formats_male.items()
)
_FORMATS_FEMALE: WeightedList[str] = WeightedList(
    PersonProviderEnUS.formats_female.items()
)
_FORMATS_NON_BINARY: WeightedList[str] = WeightedList(
    PersonProviderEnUS.formats_nonbinary.items()
)
_FORMATS = _FORMATS_MALE + _FORMATS_FEMALE
_FIRST_NAMES_MALE: WeightedList[str] = WeightedList(
    PersonProviderEnUS.first_names_male.items()
)
_FIRST_NAMES_FEMALE: WeightedList[str] = WeightedList(
    PersonProviderEnUS.first_names_female.items()
)
_FIRST_NAMES = _FORMATS_MALE + _FIRST_NAMES_FEMALE
_FIRST_NAMES_NONBINARY = _FIRST_NAMES_MALE + _FIRST_NAMES_FEMALE
_LAST_NAMES: WeightedList[str] = WeightedList(
    PersonProviderEnUS.last_names.items()
)
_PREFIXES_MALE: WeightedList[str] = WeightedList(
    PersonProviderEnUS.prefixes_male.items()
)
_PREFIXES_FEMALE: WeightedList[str] = WeightedList(
    PersonProviderEnUS.prefixes_female.items()
)
_PREFIXES_NONBINARY: WeightedList[str] = WeightedList(
    PersonProviderEnUS.prefixes_nonbinary.items()
)
_SUFFIXES_MALE: WeightedList[str] = WeightedList(
    PersonProviderEnUS.suffixes_male.items()
)
_SUFFIXES_FEMALE: WeightedList[str] = WeightedList(
    PersonProviderEnUS.suffixes_female.items()
)
_SUFFIXES_NONBINARY: WeightedList[str] = WeightedList(
    PersonProviderEnUS.suffixes_nonbinary.items()
)

# simple


first_names_male = weighted_samples(_FIRST_NAMES_MALE)
first_names_female = weighted_samples(_FIRST_NAMES_FEMALE)
first_names_nonbinary = weighted_samples(_FIRST_NAMES_NONBINARY)
first_names = weighted_samples(_FIRST_NAMES)
last_names = weighted_samples(_LAST_NAMES)
last_names_male = last_names
last_names_female = last_names
last_names_nonbinary = last_names
prefixes_male = weighted_samples(_PREFIXES_MALE)
prefixes_female = weighted_samples(_PREFIXES_FEMALE)
prefixes_nonbinary = weighted_samples(_PREFIXES_NONBINARY)
prefixes = prefixes_male | prefixes_female | prefixes_nonbinary
suffixes_male = weighted_samples(_SUFFIXES_MALE)
suffixes_female = weighted_samples(_SUFFIXES_FEMALE)
suffixes_nonbinary = weighted_samples(_SUFFIXES_NONBINARY)
suffixes = suffixes_male | suffixes_female | suffixes_nonbinary
language_names = sampled_from(_LANGUAGE_NAMES)


# name


def _build_names_strategy(formats: WeightedList[str]) -> SearchStrategy[str]:
    @composite
    def inner(draw: Callable[[SearchStrategy[T]], T]) -> str:
        format_ = draw(weighted_samples(formats))
        tokens = PATTERN_FOR_DOUBLE_BRACES.findall(format_)
        strategies = {token: _TOKENS_TO_STRATEGIES[token] for token in tokens}
        replacements = draw(fixed_dictionaries(strategies))
        return fill_format_string(format_, replacements)

    return inner()


_TOKENS_TO_STRATEGIES = {
    "first_name_female": first_names_female,
    "first_name_male": first_names_male,
    "first_name_nonbinary": first_names_nonbinary,
    "last_name": last_names,
    "prefix_female": prefixes_female,
    "prefix_male": prefixes_male,
    "prefix_nonbinary": prefixes_nonbinary,
    "suffix_female": suffixes_female,
    "suffix_male": suffixes_male,
    "suffix_nonbinary": suffixes_nonbinary,
}


names_male = _build_names_strategy(_FORMATS_MALE)
names_female = _build_names_strategy(_FORMATS_FEMALE)
names_nonbinary = _build_names_strategy(_FORMATS_NON_BINARY)
names = _build_names_strategy(_FORMATS)
