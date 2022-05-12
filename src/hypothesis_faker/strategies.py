import datetime as dt
from decimal import Decimal
from typing import Any
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Union
from uuid import UUID

from faker.providers.credit_card import CardType
from faker.providers.python import TypesSpec
from faker.typing import GenderType
from faker.typing import HueType
from hypothesis.strategies import SearchStrategy

from hypothesis_faker.providers import Provider


# address #####################################################################


def addresses() -> SearchStrategy[str]:
    return Provider.address.get_strategy()


def building_numbers() -> SearchStrategy[str]:
    return Provider.building_number.get_strategy()


def cities() -> SearchStrategy[str]:
    return Provider.city.get_strategy()


def city_suffixes() -> SearchStrategy[str]:
    return Provider.city_suffix.get_strategy()


def countries() -> SearchStrategy[str]:
    return Provider.country.get_strategy()


def country_codes(*, representation: str = "alpha-2") -> SearchStrategy[str]:
    return Provider.country_code.get_strategy(representation=representation)


def current_countries() -> SearchStrategy[str]:
    return Provider.current_country.get_strategy()


def current_country_codes() -> SearchStrategy[str]:
    return Provider.current_country_code.get_strategy()


def postcodes() -> SearchStrategy[str]:
    return Provider.postcode.get_strategy()


def street_addresses() -> SearchStrategy[str]:
    return Provider.street_address.get_strategy()


def street_names() -> SearchStrategy[str]:
    return Provider.street_name.get_strategy()


def street_suffixes() -> SearchStrategy[str]:
    return Provider.street_suffix.get_strategy()


# automotive ##################################################################


def license_plates() -> SearchStrategy[str]:
    return Provider.license_plate.get_strategy()


# bank ########################################################################


def abas() -> SearchStrategy[str]:
    return Provider.aba.get_strategy()


def bank_countries() -> SearchStrategy[str]:
    return Provider.bank_country.get_strategy()


def bbans() -> SearchStrategy[str]:
    return Provider.bban.get_strategy()


def ibans() -> SearchStrategy[str]:
    return Provider.iban.get_strategy()


def swifts(
    *,
    length: Optional[int] = None,
    primary: bool = False,
    use_dataset: bool = False,
) -> SearchStrategy[str]:
    return Provider.swift.get_strategy(
        length=length, primary=primary, use_dataset=use_dataset
    )


def swift11s(
    *, primary: bool = False, use_dataset: bool = False
) -> SearchStrategy[str]:
    return Provider.swift11.get_strategy(
        primary=primary, use_dataset=use_dataset
    )


def swift8s(*, use_dataset: bool = False) -> SearchStrategy[str]:
    return Provider.swift8.get_strategy(use_dataset=use_dataset)


# barcode #####################################################################


def eans(
    *,
    length: int = 13,
    prefixes: Tuple[Union[int, str, Tuple[Union[int, str], ...]], ...] = (),
) -> SearchStrategy[str]:
    return Provider.ean.get_strategy(length=length, prefixes=prefixes)


def ean13s(
    *, prefixes: Tuple[Union[int, str, Tuple[Union[int, str], ...]], ...] = ()
) -> SearchStrategy[str]:
    return Provider.ean13.get_strategy(prefixes=prefixes)


def ean8s(*, prefixes: Tuple[()] = ()) -> SearchStrategy[str]:
    return Provider.ean8.get_strategy(prefixes=prefixes)


def localized_eans(*, length: int = 13) -> SearchStrategy[str]:
    return Provider.localized_ean.get_strategy(length=length)


def localized_ean13s() -> SearchStrategy[str]:
    return Provider.localized_ean13.get_strategy()


def localized_ean8s() -> SearchStrategy[str]:
    return Provider.localized_ean8.get_strategy()


# color #######################################################################


def colors(
    *,
    hue: Optional[HueType] = None,
    luminosity: Optional[str] = None,
    color_format: str = "hex",
) -> SearchStrategy[str]:
    return Provider.color.get_strategy(
        hue=hue, luminosity=luminosity, color_format=color_format
    )


def color_names() -> SearchStrategy[str]:
    return Provider.color_name.get_strategy()


def hex_colors() -> SearchStrategy[str]:
    return Provider.hex_color.get_strategy()


def rgb_colors() -> SearchStrategy[str]:
    return Provider.rgb_color.get_strategy()


def rgb_css_colors() -> SearchStrategy[str]:
    return Provider.rgb_css_color.get_strategy()


def safe_color_names() -> SearchStrategy[str]:
    return Provider.safe_color_name.get_strategy()


# company #################################################################


def bss() -> SearchStrategy[str]:
    return Provider.bs.get_strategy()


def catch_phrases() -> SearchStrategy[str]:
    return Provider.catch_phrase.get_strategy()


def companies() -> SearchStrategy[str]:
    return Provider.company.get_strategy()


def company_suffixes() -> SearchStrategy[str]:
    return Provider.company_suffix.get_strategy()


# credit card #############################################################


def credit_card_expires(
    *,
    start: Union[dt.date, dt.datetime, dt.timedelta, str, int] = "now",
    end: Union[dt.date, dt.datetime, dt.timedelta, str, int] = "+10y",
    date_format: str = "%m/%y",
) -> SearchStrategy[str]:
    return Provider.credit_card_expire.get_strategy(
        start=start, end=end, date_format=date_format
    )


def credit_cards_full(
    *, card_type: Optional[CardType] = None
) -> SearchStrategy[str]:
    return Provider.credit_card_full.get_strategy(card_type=card_type)


def credit_card_numbers(
    *, card_type: Optional[CardType] = None
) -> SearchStrategy[str]:
    return Provider.credit_card_number.get_strategy(card_type=card_type)


def credit_card_providers(
    *, card_type: Optional[CardType] = None
) -> SearchStrategy[str]:
    return Provider.credit_card_provider.get_strategy(card_type=card_type)


def credit_card_security_codes(
    *, card_type: Optional[CardType] = None
) -> SearchStrategy[str]:
    return Provider.credit_card_security_code.get_strategy(card_type=card_type)


# currency ################################################################


def cryptocurrencies() -> SearchStrategy[Tuple[str, str]]:
    return Provider.cryptocurrency.get_strategy()


def cryptocurrency_codes() -> SearchStrategy[str]:
    return Provider.cryptocurrency_code.get_strategy()


def cryptocurrency_names() -> SearchStrategy[str]:
    return Provider.cryptocurrency_name.get_strategy()


def currencies() -> SearchStrategy[str]:
    return Provider.currency.get_strategy()


def currency_codes() -> SearchStrategy[str]:
    return Provider.currency_code.get_strategy()


def currency_names() -> SearchStrategy[str]:
    return Provider.currency_name.get_strategy()


def currency_symbols(*, code: Optional[str] = None) -> SearchStrategy[str]:
    return Provider.currency_symbol.get_strategy(code=code)


def pricetags() -> SearchStrategy[str]:
    return Provider.pricetag.get_strategy()


# date_time ###############################################################


def am_pms() -> SearchStrategy[str]:
    return Provider.am_pm.get_strategy()


def centuries() -> SearchStrategy[str]:
    return Provider.century.get_strategy()


def dates(
    *,
    pattern: str = "%Y-%m-%d",
    end_datetime: Union[
        dt.date, dt.datetime, dt.timedelta, str, int, None
    ] = None,
) -> SearchStrategy[str]:
    return Provider.date.get_strategy(
        pattern=pattern, end_datetime=end_datetime
    )


def dates_between(
    *,
    start_date: Union[dt.date, dt.datetime, dt.timedelta, str, int] = "-30y",
    end_date: Union[dt.date, dt.datetime, dt.timedelta, str, int] = "today",
) -> SearchStrategy[dt.date]:
    return Provider.date_between.get_strategy(
        start_date=start_date, end_date=end_date
    )


def date_between_dates(
    *,
    date_start: Union[
        dt.date, dt.datetime, dt.timedelta, str, int, None
    ] = None,
    date_end: Union[dt.date, dt.datetime, dt.timedelta, str, int, None] = None,
) -> SearchStrategy[dt.date]:
    return Provider.date_between_dates.get_strategy(
        date_start=date_start, date_end=date_end
    )


def date_objects(
    *, end_datetime: Optional[dt.datetime] = None
) -> SearchStrategy[dt.date]:
    return Provider.date_object.get_strategy(end_datetime=end_datetime)


def dates_of_birth(
    *,
    tzinfo: Optional[dt.tzinfo] = None,
    minimum_age: int = 0,
    maximum_age: int = 115,
) -> SearchStrategy[dt.date]:
    return Provider.date_of_birth.get_strategy(
        tzinfo=tzinfo, minimum_age=minimum_age, maximum_age=maximum_age
    )


def dates_this_century(
    *, before_today: bool = True, after_today: bool = False
) -> SearchStrategy[dt.date]:
    return Provider.date_this_century.get_strategy(
        before_today=before_today, after_today=after_today
    )


def dates_this_decade(
    *, before_today: bool = True, after_today: bool = False
) -> SearchStrategy[dt.date]:
    return Provider.date_this_decade.get_strategy(
        before_today=before_today, after_today=after_today
    )


def dates_this_month(
    *, before_today: bool = True, after_today: bool = False
) -> SearchStrategy[dt.date]:
    return Provider.date_this_month.get_strategy(
        before_today=before_today, after_today=after_today
    )


def dates_this_year(
    *, before_today: bool = True, after_today: bool = False
) -> SearchStrategy[dt.date]:
    return Provider.date_this_year.get_strategy(
        before_today=before_today, after_today=after_today
    )


def date_time(
    *,
    tzinfo: Optional[dt.tzinfo] = None,
    end_datetime: Union[
        dt.date, dt.datetime, dt.timedelta, str, int, None
    ] = None,
) -> SearchStrategy[dt.datetime]:
    return Provider.date_time.get_strategy(
        tzinfo=tzinfo, end_datetime=end_datetime
    )


def date_times_ad(
    *,
    tzinfo: Optional[dt.tzinfo] = None,
    end_datetime: Union[
        dt.date, dt.datetime, dt.timedelta, str, int, None
    ] = None,
    start_datetime: Union[
        dt.date, dt.datetime, dt.timedelta, str, int, None
    ] = None,
) -> SearchStrategy[dt.datetime]:
    return Provider.date_time_ad.get_strategy(
        tzinfo=tzinfo, end_datetime=end_datetime, start_datetime=start_datetime
    )


def date_times_between(
    *,
    start_date: Union[dt.date, dt.datetime, dt.timedelta, str, int] = "-30y",
    end_date: Union[dt.date, dt.datetime, dt.timedelta, str, int] = "now",
    tzinfo: Optional[dt.tzinfo] = None,
) -> SearchStrategy[dt.datetime]:
    return Provider.date_time_between.get_strategy(
        start_date=start_date, end_date=end_date, tzinfo=tzinfo
    )


def date_times_between_dates(
    *,
    datetime_start: Union[
        dt.date, dt.datetime, dt.timedelta, str, int, None
    ] = None,
    datetime_end: Union[
        dt.date, dt.datetime, dt.timedelta, str, int, None
    ] = None,
    tzinfo: Optional[dt.tzinfo] = None,
) -> SearchStrategy[dt.datetime]:
    return Provider.date_time_between_dates.get_strategy(
        datetime_start=datetime_start, datetime_end=datetime_end, tzinfo=tzinfo
    )


def date_times_this_century(
    *,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[dt.tzinfo] = None,
) -> SearchStrategy[dt.datetime]:
    return Provider.date_time_this_century.get_strategy(
        before_now=before_now, after_now=after_now, tzinfo=tzinfo
    )


def date_times_this_decade(
    *,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[dt.tzinfo] = None,
) -> SearchStrategy[dt.datetime]:
    return Provider.date_time_this_decade.get_strategy(
        before_now=before_now, after_now=after_now, tzinfo=tzinfo
    )


def date_times_this_month(
    *,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[dt.tzinfo] = None,
) -> SearchStrategy[dt.datetime]:
    return Provider.date_time_this_month.get_strategy(
        before_now=before_now, after_now=after_now, tzinfo=tzinfo
    )


def date_times_this_year(
    *,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[dt.tzinfo] = None,
) -> SearchStrategy[dt.datetime]:
    return Provider.date_time_this_year.get_strategy(
        before_now=before_now, after_now=after_now, tzinfo=tzinfo
    )


def days_of_month() -> SearchStrategy[str]:
    return Provider.day_of_month.get_strategy()


def days_of_week() -> SearchStrategy[str]:
    return Provider.day_of_week.get_strategy()


def future_dates(
    *,
    end_date: Union[dt.date, dt.datetime, dt.timedelta, str, int] = "+30d",
    tzinfo: Optional[dt.tzinfo] = None,
) -> SearchStrategy[dt.date]:
    return Provider.future_date.get_strategy(end_date=end_date, tzinfo=tzinfo)


def future_datetimes(
    *,
    end_date: Union[dt.date, dt.datetime, dt.timedelta, str, int] = "+30d",
    tzinfo: Optional[dt.tzinfo] = None,
) -> SearchStrategy[dt.datetime]:
    return Provider.future_datetime.get_strategy(
        end_date=end_date, tzinfo=tzinfo
    )


def iso8601s(
    *,
    tzinfo: Optional[dt.tzinfo] = None,
    end_datetime: Union[
        dt.date, dt.datetime, dt.timedelta, str, int, None
    ] = None,
) -> SearchStrategy[str]:
    return Provider.iso8601.get_strategy(
        tzinfo=tzinfo, end_datetime=end_datetime
    )


def months() -> SearchStrategy[str]:
    return Provider.month.get_strategy()


def month_names() -> SearchStrategy[str]:
    return Provider.month_name.get_strategy()


def past_dates(
    *,
    start_date: Union[dt.date, dt.datetime, dt.timedelta, str, int] = "-30d",
    tzinfo: Optional[dt.tzinfo] = None,
) -> SearchStrategy[dt.date]:
    return Provider.past_date.get_strategy(start_date=start_date, tzinfo=tzinfo)


def past_datetime(
    *,
    start_date: Union[dt.date, dt.datetime, dt.timedelta, str, int] = "-30d",
    tzinfo: Optional[dt.tzinfo] = None,
) -> SearchStrategy[dt.datetime]:
    return Provider.past_datetime.get_strategy(
        start_date=start_date, tzinfo=tzinfo
    )


def pytimezones(
    *args: Any, **kwargs: Any
) -> SearchStrategy[Optional[dt.tzinfo]]:
    return Provider.pytimezone.get_strategy(*args, **kwargs)


def times(
    *,
    pattern: str = "%H:%M:%S",
    end_datetime: Union[
        dt.date, dt.datetime, dt.timedelta, str, int, None
    ] = None,
) -> SearchStrategy[str]:
    return Provider.time.get_strategy(
        pattern=pattern, end_datetime=end_datetime
    )


def time_deltas(
    *,
    end_datetime: Union[
        dt.date, dt.datetime, dt.timedelta, str, int, None
    ] = None,
) -> SearchStrategy[dt.timedelta]:
    return Provider.time_delta.get_strategy(end_datetime=end_datetime)


def time_objects(
    *,
    end_datetime: Union[
        dt.date, dt.datetime, dt.timedelta, str, int, None
    ] = None,
) -> SearchStrategy[dt.time]:
    return Provider.time_object.get_strategy(end_datetime=end_datetime)


def time_series(
    *,
    start_date: Union[dt.date, dt.datetime, dt.timedelta, str, int] = "-30d",
    end_date: Union[dt.date, dt.datetime, dt.timedelta, str, int] = "now",
    precision: Optional[float] = None,
    distrib: Optional[Callable[[dt.datetime], float]] = None,
    tzinfo: Optional[dt.tzinfo] = None,
) -> SearchStrategy[Iterator[Tuple[dt.datetime, Any]]]:
    return Provider.time_series.get_strategy(
        start_date=start_date,
        end_date=end_date,
        precision=precision,
        distrib=distrib,
        tzinfo=tzinfo,
    )


def timezones() -> SearchStrategy[str]:
    return Provider.timezone.get_strategy()


def unix_times(
    *,
    end_datetime: Union[
        dt.date, dt.datetime, dt.timedelta, str, int, None
    ] = None,
    start_datetime: Union[
        dt.date, dt.datetime, dt.timedelta, str, int, None
    ] = None,
) -> SearchStrategy[int]:
    return Provider.unix_time.get_strategy(
        end_datetime=end_datetime, start_datetime=start_datetime
    )


def years() -> SearchStrategy[str]:
    return Provider.year.get_strategy()


# file ####################################################################


def file_extensions(*, category: Optional[str] = None) -> SearchStrategy[str]:
    return Provider.file_extension.get_strategy(category=category)


def file_names(
    *, category: Optional[str] = None, extension: Optional[str] = None
) -> SearchStrategy[str]:
    return Provider.file_name.get_strategy(
        category=category, extension=extension
    )


def file_paths(
    *,
    depth: int = 1,
    category: Optional[str] = None,
    extension: Optional[str] = None,
) -> SearchStrategy[str]:
    return Provider.file_path.get_strategy(
        depth=depth, category=category, extension=extension
    )


def mime_types(*, category: Optional[str] = None) -> SearchStrategy[str]:
    return Provider.mime_type.get_strategy(category=category)


def unix_devices(*, prefix: Optional[str] = None) -> SearchStrategy[str]:
    return Provider.unix_device.get_strategy(prefix=prefix)


def unix_partitions(*, prefix: Optional[str] = None) -> SearchStrategy[str]:
    return Provider.unix_partition.get_strategy(prefix=prefix)


# geo #########################################################################


def coordinates(
    *, center: Optional[float] = None, radius: Union[float, int] = 0.001
) -> SearchStrategy[Decimal]:
    return Provider.coordinate.get_strategy(center=center, radius=radius)


# internet ####################################################################


def ascii_company_emails() -> SearchStrategy[str]:
    return Provider.ascii_company_email.get_strategy()


def ascii_emails() -> SearchStrategy[str]:
    return Provider.ascii_email.get_strategy()


def ascii_free_emails() -> SearchStrategy[str]:
    return Provider.ascii_free_email.get_strategy()


def ascii_safe_emails() -> SearchStrategy[str]:
    return Provider.ascii_safe_email.get_strategy()


def company_emails() -> SearchStrategy[str]:
    return Provider.company_email.get_strategy()


def dgas(
    *,
    year: Optional[int] = None,
    month: Optional[int] = None,
    day: Optional[int] = None,
    tld: Optional[str] = None,
    length: Optional[int] = None,
) -> SearchStrategy[str]:
    return Provider.dga.get_strategy(
        year=year, month=month, day=day, tld=tld, length=length
    )


def domain_names(*, levels: int = 1) -> SearchStrategy[str]:
    return Provider.domain_name.get_strategy(levels=levels)


def domain_words() -> SearchStrategy[str]:
    return Provider.domain_word.get_strategy()


def emails(
    *, safe: bool = True, domain: Optional[str] = None
) -> SearchStrategy[str]:
    return Provider.email.get_strategy(safe=safe, domain=domain)


def free_emails() -> SearchStrategy[str]:
    return Provider.free_email.get_strategy()


def free_email_domains() -> SearchStrategy[str]:
    return Provider.free_email_domain.get_strategy()


def hostnames(*, levels: int = 1) -> SearchStrategy[str]:
    return Provider.hostname.get_strategy(levels=levels)


def http_methods() -> SearchStrategy[str]:
    return Provider.http_method.get_strategy()


def iana_ids() -> SearchStrategy[str]:
    return Provider.iana_id.get_strategy()


def image_urls(
    *,
    width: Optional[int] = None,
    height: Optional[int] = None,
    placeholder_url: Optional[str] = None,
) -> SearchStrategy[str]:
    return Provider.image_url.get_strategy(
        width=width, height=height, placeholder_url=placeholder_url
    )


def ipv4s(
    *,
    network: bool = False,
    address_class: Optional[str] = None,
    private: Optional[str] = None,
) -> SearchStrategy[str]:
    return Provider.ipv4.get_strategy(
        network=network, address_class=address_class, private=private
    )


def ipv4_network_classes() -> SearchStrategy[str]:
    return Provider.ipv4_network_class.get_strategy()


def ipv4_privates(
    *, network: bool = False, address_class: Optional[str] = None
) -> SearchStrategy[str]:
    return Provider.ipv4_private.get_strategy(
        network=network, address_class=address_class
    )


def ipv4_publics(
    *, network: bool = False, address_class: Optional[str] = None
) -> SearchStrategy[str]:
    return Provider.ipv4_public.get_strategy(
        network=network, address_class=address_class
    )


def ipv6s(*, network: bool = False) -> SearchStrategy[str]:
    return Provider.ipv6.get_strategy(network=network)


def mac_addresses() -> SearchStrategy[str]:
    return Provider.mac_address.get_strategy()


def nic_handles(*, suffix: str = "FAKE") -> SearchStrategy[str]:
    return Provider.nic_handle.get_strategy(suffix=suffix)


def nic_handle_lists(
    *, count: int = 1, suffix: str = "????"
) -> SearchStrategy[str]:
    return Provider.nic_handles.get_strategy(count=count, suffix=suffix)


def port_numbers(
    *, is_system: bool = False, is_user: bool = False, is_dynamic: bool = False
) -> SearchStrategy[int]:
    return Provider.port_number.get_strategy(
        is_system=is_system, is_user=is_user, is_dynamic=is_dynamic
    )


def ripe_ids() -> SearchStrategy[str]:
    return Provider.ripe_id.get_strategy()


def safe_domain_names() -> SearchStrategy[str]:
    return Provider.safe_domain_name.get_strategy()


def safe_emails() -> SearchStrategy[str]:
    return Provider.safe_email.get_strategy()


def slugs(*, value: Optional[str] = None) -> SearchStrategy[str]:
    return Provider.slug.get_strategy(value=value)


def tlds() -> SearchStrategy[str]:
    return Provider.tld.get_strategy()


def uris() -> SearchStrategy[str]:
    return Provider.uri.get_strategy()


def uri_extensions() -> SearchStrategy[str]:
    return Provider.uri_extension.get_strategy()


def uri_pages() -> SearchStrategy[str]:
    return Provider.uri_page.get_strategy()


def uri_paths(*, deep: Optional[int] = None) -> SearchStrategy[str]:
    return Provider.uri_path.get_strategy(deep=deep)


def urls(*, schemes: Optional[List[str]] = None) -> SearchStrategy[str]:
    return Provider.url.get_strategy(schemes=schemes)


def user_names() -> SearchStrategy[str]:
    return Provider.user_name.get_strategy()


# isbn ########################################################################


def isbn10s(*, separator: str = "-") -> SearchStrategy[str]:
    return Provider.isbn10.get_strategy(separator=separator)


def isbn13s(*, separator: str = "-") -> SearchStrategy[str]:
    return Provider.isbn13.get_strategy(separator=separator)


# job #########################################################################


def jobs() -> SearchStrategy[str]:
    return Provider.job.get_strategy()


# lorem #######################################################################


def paragraphs(
    *,
    nb_sentences: int = 3,
    variable_nb_sentences: bool = True,
    ext_word_list: Optional[Sequence[str]] = None,
) -> SearchStrategy[str]:
    return Provider.paragraph.get_strategy(
        nb_sentences=nb_sentences,
        variable_nb_sentences=variable_nb_sentences,
        ext_word_list=ext_word_list,
    )


def paragraph_lists(
    *, nb: int = 3, ext_word_list: Optional[Sequence[str]] = None
) -> SearchStrategy[List[str]]:
    return Provider.paragraphs.get_strategy(nb=nb, ext_word_list=ext_word_list)


def sentences(
    *,
    nb_words: int = 6,
    variable_nb_words: bool = True,
    ext_word_list: Optional[Sequence[str]] = None,
) -> SearchStrategy[str]:
    return Provider.sentence.get_strategy(
        nb_words=nb_words,
        variable_nb_words=variable_nb_words,
        ext_word_list=ext_word_list,
    )


def sentence_lists(
    *, nb: int = 3, ext_word_list: Optional[Sequence[str]] = None
) -> SearchStrategy[List[str]]:
    return Provider.sentences.get_strategy(nb=nb, ext_word_list=ext_word_list)


def texts(
    *, max_nb_chars: int = 200, ext_word_list: Optional[Sequence[str]] = None
) -> SearchStrategy[str]:
    return Provider.text.get_strategy(
        max_nb_chars=max_nb_chars, ext_word_list=ext_word_list
    )


def text_lists(
    *,
    nb_texts: int = 3,
    max_nb_chars: int = 200,
    ext_word_list: Optional[Sequence[str]] = None,
) -> SearchStrategy[List[str]]:
    return Provider.texts.get_strategy(
        nb_texts=nb_texts,
        max_nb_chars=max_nb_chars,
        ext_word_list=ext_word_list,
    )


def words(
    *,
    part_of_speech: Optional[str] = None,
    ext_word_list: Optional[Sequence[str]] = None,
) -> SearchStrategy[str]:
    return Provider.word.get_strategy(
        part_of_speech=part_of_speech, ext_word_list=ext_word_list
    )


def word_lists(
    *,
    nb: int = 3,
    part_of_speech: Optional[str] = None,
    ext_word_list: Optional[Sequence[str]] = None,
    unique: bool = False,
) -> SearchStrategy[List[str]]:
    return Provider.words.get_strategy(
        nb=nb,
        part_of_speech=part_of_speech,
        ext_word_list=ext_word_list,
        unique=unique,
    )


# misc ########################################################################


def binaries(*, length: int = 1048576) -> SearchStrategy[bytes]:
    return Provider.binary.get_strategy(length=length)


def booleans(*, chance_of_getting_true: int = 50) -> SearchStrategy[bool]:
    return Provider.boolean.get_strategy(
        chance_of_getting_true=chance_of_getting_true
    )


def csvs(
    *,
    header: Optional[Sequence[str]] = None,
    data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
    num_rows: int = 10,
    include_row_ids: bool = False,
) -> SearchStrategy[str]:
    return Provider.csv.get_strategy(
        header=header,
        data_columns=data_columns,
        num_rows=num_rows,
        include_row_ids=include_row_ids,
    )


def dsvs(
    *,
    dialect: str = "faker-csv",
    header: Optional[Sequence[str]] = None,
    data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
    num_rows: int = 10,
    include_row_ids: bool = False,
    **fmtparams: Any,
) -> SearchStrategy[str]:
    return Provider.dsv.get_strategy(
        dialect=dialect,
        header=header,
        data_columns=data_columns,
        num_rows=num_rows,
        include_row_ids=include_row_ids,
        **fmtparams,
    )


def fixed_widths(
    *,
    data_columns: Optional[List[Any]] = None,
    num_rows: int = 10,
    align: str = "left",
) -> SearchStrategy[str]:
    return Provider.fixed_width.get_strategy(
        data_columns=data_columns, num_rows=num_rows, align=align
    )


def images(
    *,
    size: Tuple[int, int] = (256, 256),
    image_format: str = "png",
    hue: Union[int, Sequence[int], str, None] = None,
    luminosity: Optional[str] = None,
) -> SearchStrategy[bytes]:
    return Provider.image.get_strategy(
        size=size, image_format=image_format, hue=hue, luminosity=luminosity
    )


def jsons(
    *,
    data_columns: Optional[List[Any]] = None,
    num_rows: int = 10,
    indent: Optional[int] = None,
) -> SearchStrategy[str]:
    return Provider.json.get_strategy(
        data_columns=data_columns, num_rows=num_rows, indent=indent
    )


def md5s(*, raw_output: bool = False) -> SearchStrategy[Union[bytes, str]]:
    return Provider.md5.get_strategy(raw_output=raw_output)


def null_booleans() -> SearchStrategy[Optional[bool]]:
    return Provider.null_boolean.get_strategy()


def passwords(
    *,
    length: int = 10,
    special_chars: bool = True,
    digits: bool = True,
    upper_case: bool = True,
    lower_case: bool = True,
) -> SearchStrategy[str]:
    return Provider.password.get_strategy(
        length=length,
        special_chars=special_chars,
        digits=digits,
        upper_case=upper_case,
        lower_case=lower_case,
    )


def psvs(
    *,
    header: Optional[Sequence[str]] = None,
    data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
    num_rows: int = 10,
    include_row_ids: bool = False,
) -> SearchStrategy[str]:
    return Provider.psv.get_strategy(
        header=header,
        data_columns=data_columns,
        num_rows=num_rows,
        include_row_ids=include_row_ids,
    )


def sha1s(*, raw_output: bool = False) -> SearchStrategy[Union[bytes, str]]:
    return Provider.sha1.get_strategy(raw_output=raw_output)


def sha256s(*, raw_output: bool = False) -> SearchStrategy[Union[bytes, str]]:
    return Provider.sha256.get_strategy(raw_output=raw_output)


def tars(
    *,
    uncompressed_size: int = 65536,
    num_files: int = 1,
    min_file_size: int = 4096,
    compression: Optional[str] = None,
) -> SearchStrategy[bytes]:
    return Provider.tar.get_strategy(
        uncompressed_size=uncompressed_size,
        num_files=num_files,
        min_file_size=min_file_size,
        compression=compression,
    )


def tsvs(
    *,
    header: Optional[Sequence[str]] = None,
    data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
    num_rows: int = 10,
    include_row_ids: bool = False,
) -> SearchStrategy[str]:
    return Provider.tsv.get_strategy(
        header=header,
        data_columns=data_columns,
        num_rows=num_rows,
        include_row_ids=include_row_ids,
    )


def uuid4s(
    *,
    cast_to: Optional[
        Union[Callable[[UUID], str], Callable[[UUID], bytes], None]
    ] = str,
) -> SearchStrategy[Union[bytes, str, UUID]]:
    return Provider.uuid4.get_strategy(cast_to=cast_to)


def zips(
    *,
    uncompressed_size: int = 65536,
    num_files: int = 1,
    min_file_size: int = 4096,
    compression: Optional[str] = None,
) -> SearchStrategy[str]:
    return Provider.zip.get_strategy(
        uncompressed_size=uncompressed_size,
        num_files=num_files,
        min_file_size=min_file_size,
        compression=compression,
    )


# person ######################################################################


def first_names() -> SearchStrategy[str]:
    return Provider.first_name.get_strategy()


def first_name_females() -> SearchStrategy[str]:
    return Provider.first_name_female.get_strategy()


def first_name_males() -> SearchStrategy[str]:
    return Provider.first_name_male.get_strategy()


def first_name_nonbinaries() -> SearchStrategy[str]:
    return Provider.first_name_nonbinary.get_strategy()


def language_names() -> SearchStrategy[str]:
    return Provider.language_name.get_strategy()


def last_names() -> SearchStrategy[str]:
    return Provider.last_name.get_strategy()


def last_name_females() -> SearchStrategy[str]:
    return Provider.last_name_female.get_strategy()


def last_name_males() -> SearchStrategy[str]:
    return Provider.last_name_male.get_strategy()


def last_name_nonbinaries() -> SearchStrategy[str]:
    return Provider.last_name_nonbinary.get_strategy()


def names() -> SearchStrategy[str]:
    return Provider.name_.get_strategy()


def name_females() -> SearchStrategy[str]:
    return Provider.name_female.get_strategy()


def name_males() -> SearchStrategy[str]:
    return Provider.name_male.get_strategy()


def name_nonbinaries() -> SearchStrategy[str]:
    return Provider.name_nonbinary.get_strategy()


def prefixes() -> SearchStrategy[str]:
    return Provider.prefix.get_strategy()


def prefix_females() -> SearchStrategy[str]:
    return Provider.prefix_female.get_strategy()


def prefix_males() -> SearchStrategy[str]:
    return Provider.prefix_male.get_strategy()


def prefix_nonbinaries() -> SearchStrategy[str]:
    return Provider.prefix_nonbinary.get_strategy()


def suffixes() -> SearchStrategy[str]:
    return Provider.suffix.get_strategy()


def suffix_females() -> SearchStrategy[str]:
    return Provider.suffix_female.get_strategy()


def suffix_males() -> SearchStrategy[str]:
    return Provider.suffix_male.get_strategy()


def suffix_nonbinaries() -> SearchStrategy[str]:
    return Provider.suffix_nonbinary.get_strategy()


# phone_number ################################################################


def country_calling_codes() -> SearchStrategy[str]:
    return Provider.country_calling_code.get_strategy()


def msisdns() -> SearchStrategy[str]:
    return Provider.msisdn.get_strategy()


def phone_numbers() -> SearchStrategy[str]:
    return Provider.phone_number.get_strategy()


# profile #####################################################################


def profiles(
    *, fields: Optional[List[str]] = None, sex: Optional[GenderType] = None
) -> SearchStrategy[
    Dict[str, Union[str, Tuple[Decimal, Decimal], List[str], dt.date]]
]:
    return Provider.profile.get_strategy(fields=fields, sex=sex)


def simple_profiles(
    *, sex: Optional[GenderType] = None
) -> SearchStrategy[Dict[str, Union[str, dt.date, GenderType]]]:
    return Provider.simple_profile.get_strategy(sex=sex)


# python ######################################################################


def pybools() -> SearchStrategy[bool]:
    return Provider.pybool.get_strategy()


def pydecimals(
    *,
    left_digits: Optional[int] = None,
    right_digits: Optional[int] = None,
    positive: bool = False,
    min_value: Optional[Decimal] = None,
    max_value: Optional[Decimal] = None,
) -> SearchStrategy[Decimal]:
    return Provider.pydecimal.get_strategy(
        left_digits=left_digits,
        right_digits=right_digits,
        positive=positive,
        min_value=min_value,
        max_value=max_value,
    )


def pydicts(
    nb_elements: int = 10,
    variable_nb_elements: bool = True,
    value_types: Optional[TypesSpec] = None,
    allowed_types: Optional[TypesSpec] = None,
) -> SearchStrategy[Dict[Any, Any]]:
    return Provider.pydict.get_strategy(
        nb_elements=nb_elements,
        variable_nb_elements=variable_nb_elements,
        value_types=value_types,
        allowed_types=allowed_types,
    )


def pyfloats(
    *,
    left_digits: Optional[int] = None,
    right_digits: Optional[int] = None,
    positive: bool = False,
    min_value: Optional[float] = None,
    max_value: Optional[float] = None,
) -> SearchStrategy[float]:
    return Provider.pyfloat.get_strategy(
        left_digits=left_digits,
        right_digits=right_digits,
        positive=positive,
        min_value=min_value,
        max_value=max_value,
    )


def pyints(
    *, min_value: int = 0, max_value: int = 9999, step: int = 1
) -> SearchStrategy[int]:
    return Provider.pyint.get_strategy(
        min_value=min_value, max_value=max_value, step=step
    )


def pyiterables(
    *,
    nb_elements: int = 10,
    variable_nb_elements: bool = True,
    value_types: Optional[TypesSpec] = None,
    allowed_types: Optional[TypesSpec] = None,
) -> SearchStrategy[Iterable[Any]]:
    return Provider.pyiterable.get_strategy(
        nb_elements=nb_elements,
        variable_nb_elements=variable_nb_elements,
        value_types=value_types,
        allowed_types=allowed_types,
    )


def pylists(
    *,
    nb_elements: int = 10,
    variable_nb_elements: bool = True,
    value_types: Optional[TypesSpec] = None,
    allowed_types: Optional[TypesSpec] = None,
) -> SearchStrategy[List[Any]]:
    return Provider.pylist.get_strategy(
        nb_elements=nb_elements,
        variable_nb_elements=variable_nb_elements,
        value_types=value_types,
        allowed_types=allowed_types,
    )


def pysets(
    *,
    nb_elements: int = 10,
    variable_nb_elements: bool = True,
    value_types: Optional[TypesSpec] = None,
    allowed_types: Optional[TypesSpec] = None,
) -> SearchStrategy[Set[Any]]:
    return Provider.pyset.get_strategy(
        nb_elements=nb_elements,
        variable_nb_elements=variable_nb_elements,
        value_types=value_types,
        allowed_types=allowed_types,
    )


def pystrs(
    *, min_chars: Optional[int] = None, max_chars: int = 20
) -> SearchStrategy[str]:
    return Provider.pystr.get_strategy(min_chars=min_chars, max_chars=max_chars)


def pystr_formats(
    *,
    string_format: str = "?#-###{{random_int}}{{random_letter}}",
    letters: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
) -> SearchStrategy[str]:
    return Provider.pystr_format.get_strategy(
        string_format=string_format, letters=letters
    )


def pystructs(
    *,
    count: int = 10,
    value_types: Optional[TypesSpec] = None,
    allowed_types: Optional[TypesSpec] = None,
) -> SearchStrategy[Tuple[List[Any], Dict[Any, Any], Dict[Any, Any]]]:
    return Provider.pystruct.get_strategy(
        count=count, value_types=value_types, allowed_types=allowed_types
    )


def pytuples(
    *,
    nb_elements: int = 10,
    variable_nb_elements: bool = True,
    value_types: Optional[TypesSpec] = None,
    allowed_types: Optional[TypesSpec] = None,
) -> SearchStrategy[Tuple[Any, ...]]:
    return Provider.pytuple.get_strategy(
        nb_elements=nb_elements,
        variable_nb_elements=variable_nb_elements,
        value_types=value_types,
        allowed_types=allowed_types,
    )


# ssn #########################################################################


def ssns() -> SearchStrategy[str]:
    return Provider.ssn.get_strategy()


# user_agent ##################################################################


def android_platform_tokens() -> SearchStrategy[str]:
    return Provider.android_platform_token.get_strategy()


def chromes(
    *,
    version_from: int = 13,
    version_to: int = 63,
    build_from: int = 800,
    build_to: int = 899,
) -> SearchStrategy[str]:
    return Provider.chrome.get_strategy(
        version_from=version_from,
        version_to=version_to,
        build_from=build_from,
        build_to=build_to,
    )


def firefoxes() -> SearchStrategy[str]:
    return Provider.firefox.get_strategy()


def internet_explorers() -> SearchStrategy[str]:
    return Provider.internet_explorer.get_strategy()


def ios_platform_tokens() -> SearchStrategy[str]:
    return Provider.ios_platform_token.get_strategy()


def linux_platform_tokens() -> SearchStrategy[str]:
    return Provider.linux_platform_token.get_strategy()


def linux_processors() -> SearchStrategy[str]:
    return Provider.linux_processor.get_strategy()


def mac_platform_tokens() -> SearchStrategy[str]:
    return Provider.mac_platform_token.get_strategy()


def mac_processors() -> SearchStrategy[str]:
    return Provider.mac_processor.get_strategy()


def operas() -> SearchStrategy[str]:
    return Provider.opera.get_strategy()


def safaris() -> SearchStrategy[str]:
    return Provider.safari.get_strategy()


def user_agents() -> SearchStrategy[str]:
    return Provider.user_agent.get_strategy()


def windows_platform_tokens() -> SearchStrategy[str]:
    return Provider.windows_platform_token.get_strategy()
