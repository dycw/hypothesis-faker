from typing import Callable
from typing import Iterable
from typing import Optional
from typing import Union

from hypothesis import given
from hypothesis.strategies import DataObject
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import data
from hypothesis.strategies import iterables
from hypothesis.strategies import none
from hypothesis.strategies import sampled_from
from pytest import mark

from hypothesis_faker.providers.file import _FILE_EXTENSIONS
from hypothesis_faker.providers.file import _MIME_TYPES
from hypothesis_faker.providers.file import file_extensions
from hypothesis_faker.providers.file import file_names
from hypothesis_faker.providers.file import file_paths
from hypothesis_faker.providers.file import mime_types
from hypothesis_faker.providers.file import unix_devices
from hypothesis_faker.providers.file import unix_partitions
from hypothesis_faker.providers.lorem import words


_mime_type_categories = sampled_from(list(_MIME_TYPES))
_file_extension_categories = sampled_from(list(_FILE_EXTENSIONS))


@given(
    data=data(),
    category=none() | _mime_type_categories | iterables(_mime_type_categories),
)
def test_mime_types(
    data: DataObject, category: Optional[Union[str, Iterable[str]]]
) -> None:
    assert isinstance(data.draw(mime_types(category=category)), str)


@mark.parametrize("strategy", [file_names, file_paths])
@given(
    data=data(),
    category=none()
    | _file_extension_categories
    | iterables(_file_extension_categories),
    extension=none() | words,
)
def test_file_names_and_file_paths(
    strategy: Callable[..., SearchStrategy[str]],
    data: DataObject,
    category: Optional[Union[str, Iterable[str]]],
    extension: Optional[str],
) -> None:
    assert isinstance(
        data.draw(strategy(category=category, extension=extension)), str
    )


@given(
    data=data(),
    category=none()
    | _file_extension_categories
    | iterables(_file_extension_categories),
)
def test_file_extensions(
    data: DataObject, category: Optional[Union[str, Iterable[str]]]
) -> None:
    assert isinstance(data.draw(file_extensions(category=category)), str)


@given(
    data=data(),
    category=none()
    | _file_extension_categories
    | iterables(_file_extension_categories),
)
def test_file_paths(
    data: DataObject, category: Optional[Union[str, Iterable[str]]]
) -> None:
    assert isinstance(data.draw(file_extensions(category=category)), str)


@mark.parametrize("strategy", [unix_devices, unix_partitions])
@given(data=data(), prefix=none() | words)
def test_unix_devices_and_partitions(
    strategy: Callable[..., SearchStrategy[str]],
    data: DataObject,
    prefix: Optional[str],
) -> None:
    assert isinstance(data.draw(strategy(prefix=prefix)), str)
