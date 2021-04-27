from typing import Callable
from typing import TypeVar

from faker.providers.person.en import Provider as PersonEnProvider
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import composite
from hypothesis.strategies import sampled_from


T = TypeVar("T")


@composite
def _names(draw: Callable[[SearchStrategy[T]], T]) -> str:
    PersonEnProvider.first_name
    format_ = draw(sampled_from(PersonEnProvider.formats))
    return format_


names = _names()
