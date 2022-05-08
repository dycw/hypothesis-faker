from functools import lru_cache
from os import getenv
from pathlib import Path

from xdg import xdg_cache_home


HYPOTHESIS_FAKER_ROOT = "HYPOTHESIS_FAKER_ROOT"
HYPOTHESIS_FAKER_UPDATE_FREQ = "HYPOTHESIS_FAKER_UPDATE_FREQ"
HYPOTHESIS_FAKER_DURATION = "HYPOTHESIS_FAKER_DURATION"
HYPOTHESIS_FAKER_MAX_ITEMS = "HYPOTHESIS_FAKER_MAX_ITEMS"


@lru_cache(maxsize=1)
def get_root() -> Path:
    default = xdg_cache_home().joinpath("hypothesis-faker")
    return Path(getenv(HYPOTHESIS_FAKER_ROOT, default))


@lru_cache(maxsize=1)
def get_update_freq() -> float:
    return float(getenv(HYPOTHESIS_FAKER_UPDATE_FREQ, 3600.0))


@lru_cache(maxsize=1)
def get_duration() -> float:
    return float(getenv(HYPOTHESIS_FAKER_DURATION, 1.0))


@lru_cache(maxsize=1)
def get_max_items() -> int:
    return int(getenv(HYPOTHESIS_FAKER_MAX_ITEMS, 100_000))
