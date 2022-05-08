import json
from contextlib import suppress
from enum import Enum
from enum import auto
from gzip import GzipFile
from hashlib import md5
from pathlib import Path
from pickle import dump  # noqa: S403
from pickle import load  # noqa: S403
from random import shuffle
from time import time
from timeit import default_timer
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

from _pytest.compat import cached_property
from faker import Faker
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies._internal.core import sampled_from
from more_itertools import unique_everseen
from writer_cm import writer_cm

from hypothesis_faker.settings import get_duration
from hypothesis_faker.settings import get_max_items
from hypothesis_faker.settings import get_root
from hypothesis_faker.settings import get_update_freq


_ARG_HASHES: Dict[Tuple[Tuple[Any, ...], Tuple[Tuple[str, Any], ...]], str] = {}
_FAKER = Faker()
_ITEMS: Dict["Provider", List[Any]] = {}


def get_args_hash(*args: Any, **kwargs: Any) -> str:
    key = (args, tuple(sorted(kwargs.items())))
    try:
        return _ARG_HASHES[key]
    except KeyError:
        text = json.dumps((args, kwargs), sort_keys=True)
        value = _ARG_HASHES[key] = md5(text.encode()).hexdigest()  # noqa: S324
        return value


class Provider(Enum):
    # address
    address = auto()

    # geo

    coordinate = auto()

    # properties/methods ######################################################

    @cached_property
    def path(self) -> Path:
        return get_root().joinpath(self.name)

    def get_path(self, *args: Any, **kwargs: Any) -> Path:
        return self.path.joinpath(get_args_hash(*args, **kwargs))

    def get_update_time(self, *args: Any, **kwargs: Any) -> Optional[float]:
        path = self.get_path(*args, **kwargs)
        try:
            return path.stat().st_mtime
        except (FileNotFoundError, NotADirectoryError):
            return None

    def needs_update(self, *args: Any, **kwargs: Any) -> bool:
        ut = self.get_update_time(*args, **kwargs)
        return (ut is None) or ((time() - ut) >= get_update_freq())

    def generate_items(self, *args: Any, **kwargs: Any) -> List[Any]:
        items = []
        with suppress(FileNotFoundError, NotADirectoryError):
            items.extend(self.load_items(*args, **kwargs))
        t, dur, method = (
            default_timer(),
            get_duration(),
            getattr(_FAKER, self.name),
        )
        while default_timer() - t <= dur:
            items.append(method(*args, **kwargs))
        items = list(unique_everseen(items))
        max_items = get_max_items()
        if len(items) > max_items:
            shuffle(items)
            items = items[:max_items]
        path = self.get_path(*args, **kwargs)
        with writer_cm(path, overwrite=True) as temp, GzipFile(
            temp, mode="wb"
        ) as fh:
            dump(items, fh)
        return items

    def load_items(self, *args: Any, **kwargs: Any) -> List[Any]:
        path = self.get_path(*args, **kwargs)
        with GzipFile(path, mode="rb") as fh:
            return load(fh)  # noqa: S301

    def get_items(self, *args: Any, **kwargs: Any) -> List[Any]:
        if self.needs_update(*args, **kwargs):
            items = _ITEMS[self] = self.generate_items(*args, **kwargs)
        else:
            try:
                items = _ITEMS[self]
            except KeyError:
                items = _ITEMS[self] = self.load_items(*args, **kwargs)
        return items

    def get_strategy(self, *args: Any, **kwargs: Any) -> SearchStrategy[Any]:
        items = self.get_items(*args, **kwargs)
        return sampled_from(items)
