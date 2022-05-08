from decimal import Decimal
from typing import List
from typing import Optional
from typing import Union

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
