import json
from contextlib import suppress
from enum import Enum
from enum import auto
from gzip import GzipFile
from hashlib import md5
from pathlib import Path
from pickle import dump  # noqa: S403
from pickle import load  # noqa: S403
from time import time
from timeit import default_timer
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

from backports.cached_property import cached_property
from faker import Faker
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import sampled_from
from writer_cm import writer_cm

from hypothesis_faker.settings import get_duration
from hypothesis_faker.settings import get_max_items
from hypothesis_faker.settings import get_root
from hypothesis_faker.settings import get_update_freq


_ArgsType = Tuple[Tuple[Any, ...], Tuple[Tuple[str, Any], ...]]
_ARGS_HASHES: Dict[_ArgsType, str] = {}
_FAKER = Faker()
_ITEMS: Dict[Tuple["Provider", str], List[Any]] = {}


def get_args_hash(*args: Any, **kwargs: Any) -> str:
    key = (args, tuple(sorted(kwargs.items())))
    try:
        return _ARGS_HASHES[key]
    except KeyError:
        text = json.dumps((args, kwargs), sort_keys=True)
        value = _ARGS_HASHES[key] = md5(text.encode()).hexdigest()  # noqa: S324
        return value


class Provider(Enum):
    # address #################################################################
    address = auto()
    building_number = auto()
    city = auto()
    city_suffix = auto()
    country = auto()
    country_code = auto()
    current_country = auto()
    current_country_code = auto()
    postcode = auto()
    street_address = auto()
    street_name = auto()
    street_suffix = auto()

    # automotive ##############################################################
    license_plate = auto()

    # bank ####################################################################
    aba = auto()
    bank_country = auto()
    bban = auto()
    iban = auto()
    swift = auto()
    swift11 = auto()
    swift8 = auto()

    # barcode #################################################################
    ean = auto()
    ean13 = auto()
    ean8 = auto()
    localized_ean = auto()
    localized_ean13 = auto()
    localized_ean8 = auto()

    # geo #####################################################################
    coordinate = auto()

    # internet ################################################################
    ascii_company_email = auto()
    ascii_email = auto()
    ascii_free_email = auto()
    ascii_safe_email = auto()
    company_email = auto()
    dga = auto()
    domain_name = auto()
    domain_word = auto()
    email = auto()
    free_email = auto()
    free_email_domain = auto()
    hostname = auto()
    http_method = auto()
    iana_id = auto()
    image_url = auto()
    ipv4 = auto()
    ipv4_network_class = auto()
    ipv4_private = auto()
    ipv4_public = auto()
    ipv6 = auto()
    mac_address = auto()
    nic_handle = auto()
    nic_handles = auto()
    port_number = auto()
    ripe_id = auto()
    safe_domain_name = auto()
    safe_email = auto()
    slug = auto()
    tld = auto()
    uri = auto()
    uri_extension = auto()
    uri_page = auto()
    uri_path = auto()
    url = auto()
    user_name = auto()

    # user_agent ##############################################################

    android_platform_token = auto()
    chrome = auto()
    firefox = auto()
    internet_explorer = auto()
    ios_platform_token = auto()
    linux_platform_token = auto()
    linux_processor = auto()
    mac_platform_token = auto()
    mac_processor = auto()
    opera = auto()
    safari = auto()
    user_agent = auto()
    windows_platform_token = auto()

    # properties/methods ######################################################

    @cached_property
    def path(self) -> Path:
        return get_root().joinpath(self.name)

    def get_path(self, args_hash: str) -> Path:
        return self.path.joinpath(args_hash)

    def get_update_time(self, path: Path) -> Optional[float]:
        try:
            return path.stat().st_mtime
        except (FileNotFoundError, NotADirectoryError):
            return None

    def needs_update(self, path: Path) -> bool:
        ut = self.get_update_time(path)
        return (ut is None) or ((time() - ut) >= get_update_freq())

    def generate_items(
        self, path: Path, *args: Any, **kwargs: Any
    ) -> List[Any]:
        items = []
        with suppress(FileNotFoundError, NotADirectoryError):
            items.extend(self.load_items(path))
        t, dur, method = (
            default_timer(),
            get_duration(),
            getattr(_FAKER, self.name),
        )
        while (len(items) == 0) or (default_timer() - t <= dur):
            items.append(method(*args, **kwargs))
        items = list(set(items))[: get_max_items()]
        with writer_cm(path, overwrite=True) as temp, GzipFile(
            temp, mode="wb"
        ) as fh:
            dump(items, fh)
        return items

    def load_items(self, path: Path) -> List[Any]:
        with GzipFile(path, mode="rb") as fh:
            return load(fh)  # noqa: S301

    def get_items(self, *args: Any, **kwargs: Any) -> List[Any]:
        args_hash = get_args_hash(*args, **kwargs)
        key = (self, args_hash)
        path = self.get_path(args_hash)
        if self.needs_update(path):
            items = _ITEMS[key] = self.generate_items(path, *args, **kwargs)
        else:
            try:
                items = _ITEMS[key]
            except KeyError:
                items = _ITEMS[key] = self.load_items(path)
        return items

    def get_strategy(self, *args: Any, **kwargs: Any) -> SearchStrategy[Any]:
        items = self.get_items(*args, **kwargs)
        return sampled_from(items)
