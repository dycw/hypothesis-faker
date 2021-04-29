from typing import Iterable
from typing import Union

from hypothesis import given
from hypothesis.strategies import DataObject
from hypothesis.strategies import data
from hypothesis.strategies import iterables
from hypothesis.strategies import none
from hypothesis.strategies import sampled_from

from hypothesis_faker.providers.file import _MIME_TYPES
from hypothesis_faker.providers.file import mime_types


_categories = sampled_from(list(_MIME_TYPES))


@given(data=data(), category=_categories | iterables(_categories) | none())
def test_mime_type(
    data: DataObject, category: Union[str, Iterable[str], None]
) -> None:
    assert isinstance(data.draw(mime_types(category=category)), str)
