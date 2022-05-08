import datetime as dt
import json
from contextlib import suppress
from dataclasses import dataclass
from enum import Enum
from enum import auto
from gzip import GzipFile
from hashlib import md5
from pathlib import Path
from pickle import dump  # noqa: S403
from pickle import load  # noqa: S403
from random import shuffle
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
from xdg import xdg_cache_home

from hypothesis_faker.settings import GENERATION_FREQ
from hypothesis_faker.settings import GENERATION_TIME
from hypothesis_faker.settings import MAX_ITEMS


_FREQ = dt.timedelta(seconds=GENERATION_FREQ)
_ROOT = xdg_cache_home().joinpath("hypothesis-faker")
_FAKER = Faker()
_ITEMS: Dict["Provider", List[Any]] = {}


@dataclass
class Arguments:
    """A set of arguments to be taken together."""

    args: Tuple[Any, ...]
    kwargs: Dict[str, Any]

    @cached_property
    def hash(self) -> str:
        text = json.dumps((self.args, self.kwargs), sort_keys=True)
        return md5(text.encode()).hexdigest()  # noqa: S324


class Provider(Enum):
    # address
    address = auto()

    # geo

    coordinate = auto()

    # properties/methods ######################################################

    @cached_property
    def path(self) -> Path:
        return _ROOT.joinpath(self.name)

    def get_path(self, args: Arguments) -> Path:
        return self.path.joinpath(args.hash)

    def get_update_time(self, path: Path) -> Optional[dt.datetime]:
        try:
            return dt.datetime.fromtimestamp(path.stat().st_mtime)
        except FileNotFoundError:
            return None

    def needs_update(self, path: Path) -> bool:
        ut = self.get_update_time(path)
        return (ut is None) or ((dt.datetime.now() - ut) >= _FREQ)

    def update(self, path: Path) -> List[Any]:
        items = []
        with suppress(FileNotFoundError):
            items.extend(self.load_items(path))
        t, method = default_timer(), getattr(_FAKER, self.name)
        while default_timer() - t <= GENERATION_TIME:
            items.append(method())
        items = list(unique_everseen(items))
        if len(items) > MAX_ITEMS:
            shuffle(items)
            items = items[:MAX_ITEMS]
        with writer_cm(path, overwrite=True) as temp, GzipFile(
            temp, mode="wb"
        ) as fh:
            dump(items, fh)
        return items

    def load_items(self, path: Path) -> List[Any]:
        with GzipFile(path, mode="rb") as fh:
            return load(fh)  # noqa: S301

    def get_items(self, path: Path) -> List[Any]:
        if self.needs_update(path):
            items = _ITEMS[self] = self.update(path)
        else:
            try:
                items = _ITEMS[self]
            except KeyError:
                items = _ITEMS[self] = self.load_items(path)
        return items

    def get_strategy(self, *args: Any, **kwargs: Any) -> SearchStrategy[Any]:
        arguments = Arguments(args, kwargs)
        path = self.get_path(arguments)
        items = self.get_items(path)
        return sampled_from(items)
