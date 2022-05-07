import datetime as dt
from contextlib import suppress
from enum import Enum
from enum import auto
from gzip import GzipFile
from pathlib import Path
from pickle import dump  # noqa: S403
from pickle import load  # noqa: S403
from timeit import default_timer
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from faker import Faker
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies._internal.core import sampled_from
from more_itertools import unique_everseen
from writer_cm import writer_cm

from hypothesis_faker.utilities import PATH_CACHE


_FAKER = Faker()
_ITEMS: Dict["Provider", List[Any]] = {}


class Provider(Enum):
    address = auto()

    @property
    def path(self) -> Path:
        return PATH_CACHE.joinpath(self.name)

    @property
    def last_updated(self) -> Optional[dt.datetime]:
        try:
            stat = self.path.stat()
        except FileNotFoundError:
            return None
        else:
            return dt.datetime.fromtimestamp(stat.st_mtime)

    @property
    def needs_update(self) -> bool:
        lu = self.last_updated
        return (lu is None) or (
            (dt.datetime.now() - lu) >= dt.timedelta(seconds=10)
        )

    def update(self) -> List[Any]:
        items, path = [], self.path
        with suppress(FileNotFoundError):
            items.extend(self.load_items())
        t, method = default_timer(), getattr(_FAKER, self.name)
        while default_timer() - t <= 1.0:
            items.append(method())
        items = list(unique_everseen(items))
        with writer_cm(path, overwrite=True) as temp, GzipFile(
            temp, mode="wb"
        ) as fh:
            dump(items, fh)
        return items

    def load_items(self) -> List[Any]:
        with GzipFile(self.path, mode="rb") as fh:
            return load(fh)  # noqa: S301

    def get_items(self) -> List[Any]:
        if self.needs_update:
            items = _ITEMS[self] = self.update()
        else:
            try:
                items = _ITEMS[self]
            except KeyError:
                items = _ITEMS[self] = self.load_items()
        return items

    def get_strategy(self) -> SearchStrategy[Any]:
        return sampled_from(self.load_items())
