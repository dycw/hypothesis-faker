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

    # color ###################################################################
    color = auto()
    color_name = auto()
    hex_color = auto()
    rgb_color = auto()
    rgb_css_color = auto()
    safe_color_name = auto()

    # company #################################################################
    bs = auto()
    catch_phrase = auto()
    company = auto()
    company_suffix = auto()

    # credit card #############################################################
    credit_card_expire = auto()
    credit_card_full = auto()
    credit_card_number = auto()
    credit_card_provider = auto()
    credit_card_security_code = auto()

    # currency ################################################################
    cryptocurrency = auto()
    cryptocurrency_code = auto()
    cryptocurrency_name = auto()
    currency = auto()
    currency_code = auto()
    currency_name = auto()
    currency_symbol = auto()
    pricetag = auto()

    # date_time ###############################################################
    am_pm = auto()
    century = auto()
    date = auto()
    date_between = auto()
    date_between_dates = auto()
    date_object = auto()
    date_of_birth = auto()
    date_this_century = auto()
    date_this_decade = auto()
    date_this_month = auto()
    date_this_year = auto()
    date_time = auto()
    date_time_ad = auto()
    date_time_between = auto()
    date_time_between_dates = auto()
    date_time_this_century = auto()
    date_time_this_decade = auto()
    date_time_this_month = auto()
    date_time_this_year = auto()
    day_of_month = auto()
    day_of_week = auto()
    future_date = auto()
    future_datetime = auto()
    iso8601 = auto()
    month = auto()
    month_name = auto()
    past_date = auto()
    past_datetime = auto()
    pytimezone = auto()
    time = auto()
    time_delta = auto()
    time_object = auto()
    time_series = auto()
    timezone = auto()
    unix_time = auto()
    year = auto()

    # file ####################################################################
    file_extension = auto()
    file_name = auto()
    file_path = auto()
    mime_type = auto()
    unix_device = auto()
    unix_partition = auto()

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

    # isbn ####################################################################
    isbn10 = auto()
    isbn13 = auto()

    # job #####################################################################
    job = auto()

    # lorem ###################################################################
    paragraph = auto()
    paragraphs = auto()
    sentence = auto()
    sentences = auto()
    text = auto()
    texts = auto()
    word = auto()
    words = auto()

    # misc ####################################################################
    binary = auto()
    boolean = auto()
    csv = auto()
    dsv = auto()
    fixed_width = auto()
    image = auto()
    json = auto()
    md5 = auto()
    null_boolean = auto()
    password = auto()
    psv = auto()
    sha1 = auto()
    sha256 = auto()
    tar = auto()
    tsv = auto()
    uuid4 = auto()
    zip = auto()

    # person ##################################################################
    first_name = auto()
    first_name_female = auto()
    first_name_male = auto()
    first_name_nonbinary = auto()
    language_name = auto()
    last_name = auto()
    last_name_female = auto()
    last_name_male = auto()
    last_name_nonbinary = auto()
    name_ = auto()
    name_female = auto()
    name_male = auto()
    name_nonbinary = auto()
    prefix = auto()
    prefix_female = auto()
    prefix_male = auto()
    prefix_nonbinary = auto()
    suffix = auto()
    suffix_female = auto()
    suffix_male = auto()
    suffix_nonbinary = auto()

    # phone_number ############################################################
    country_calling_code = auto()
    msisdn = auto()
    phone_number = auto()

    # profile #################################################################
    profile = auto()
    simple_profile = auto()

    # python ##################################################################
    pybool = auto()
    pydecimal = auto()
    pydict = auto()
    pyfloat = auto()
    pyint = auto()
    pyiterable = auto()
    pylist = auto()
    pyset = auto()
    pystr = auto()
    pystr_format = auto()
    pystruct = auto()
    pytuple = auto()

    # ssn #####################################################################
    ssn = auto()

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
        return get_root().joinpath(self._cleaned_name)

    @cached_property
    def _cleaned_name(self) -> str:
        return self.name.rstrip("_")

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
            getattr(_FAKER, self._cleaned_name),
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
