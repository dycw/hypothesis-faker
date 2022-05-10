from decimal import Decimal
from typing import Any
from typing import Callable
from typing import List
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Union
from uuid import UUID

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
