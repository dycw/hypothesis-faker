from itertools import chain
from typing import Iterable
from typing import Optional
from typing import Union
from typing import cast

from faker.providers.file import Provider as FileProvider
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import just
from hypothesis.strategies import one_of
from hypothesis.strategies import sampled_from
from hypothesis.strategies import tuples
from hypothesis.strategies._internal.core import lists

from hypothesis_faker.providers.lorem import words
from hypothesis_faker.types import T
from hypothesis_faker.utilities import ascii_lowercase_letters
from hypothesis_faker.utilities import digits_0_9


_MIME_TYPES = {
    "application": sampled_from(list(FileProvider.application_mime_types)),
    "audio": sampled_from(list(FileProvider.audio_mime_types)),
    "image": sampled_from(list(FileProvider.image_mime_types)),
    "message": sampled_from(list(FileProvider.message_mime_types)),
    "model": sampled_from(list(FileProvider.model_mime_types)),
    "multipart": sampled_from(list(FileProvider.multipart_mime_types)),
    "text": sampled_from(list(FileProvider.text_mime_types)),
    "video": sampled_from(list(FileProvider.video_mime_types)),
}
_FILE_EXTENSIONS = {
    "audio": sampled_from(list(FileProvider.audio_file_extensions)),
    "image": sampled_from(list(FileProvider.image_file_extensions)),
    "office": sampled_from(list(FileProvider.office_file_extensions)),
    "text": sampled_from(list(FileProvider.text_file_extensions)),
    "video": sampled_from(list(FileProvider.video_file_extensions)),
}


def mime_types(
    category: Optional[Union[str, Iterable[str]]] = None
) -> SearchStrategy[str]:
    return _strategy_from_category(_MIME_TYPES, category)


def _strategy_from_category(
    mapping: dict[str, SearchStrategy[T]],
    category: Optional[Union[str, Iterable[str]]],
) -> SearchStrategy[T]:
    if category is None:
        return one_of(*mapping.values())
    else:
        try:
            categories = set(cast(Iterable[str], category))
        except TypeError:
            return mapping[cast(str, category)]
        else:
            return one_of(*(v for k, v in mapping.items() if k in categories))


def file_names(
    category: Optional[Union[str, Iterable[str]]] = None,
    extension: Optional[str] = None,
) -> SearchStrategy[str]:
    if extension is None:
        extensions = file_extensions(category=category)
    else:
        extensions = just(extension)
    return tuples(words, extensions).map(_file_names_map)


def _file_names_map(pair: tuple) -> str:
    first, second = pair
    return ".".join([first, second])


def file_extensions(
    category: Optional[Union[str, Iterable[str]]] = None
) -> SearchStrategy[str]:
    return _strategy_from_category(_FILE_EXTENSIONS, category)


def file_paths(
    category: Optional[Union[str, Iterable[str]]] = None,
    extension: Optional[str] = None,
) -> SearchStrategy[str]:
    return tuples(
        lists(words), file_names(category=category, extension=extension)
    ).map(_file_paths_map)


def _file_paths_map(pair: tuple) -> str:
    words, filename = pair
    return "/".join(chain([""], words, [filename]))


def unix_devices(prefix: Optional[str] = None) -> SearchStrategy[str]:
    if prefix is None:
        prefixes = sampled_from(list(FileProvider.unix_device_prefixes))
    else:
        prefixes = just(prefix)
    return tuples(prefixes, ascii_lowercase_letters).map(_unix_devices_map)


def _unix_devices_map(pair: tuple) -> str:
    prefix, suffix = pair
    return "/dev/{prefix}{suffix}"


def unix_partitions(prefix: Optional[str] = None) -> SearchStrategy[str]:
    return tuples(unix_devices(prefix=prefix), digits_0_9).map(
        _unix_partitions_map
    )


def _unix_partitions_map(pair: tuple) -> str:
    return "".join(pair)
