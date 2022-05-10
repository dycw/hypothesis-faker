from decimal import Decimal
from typing import Any
from typing import Callable

from hypothesis import given
from hypothesis.strategies import DataObject
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import data
from pytest import mark
from pytest import param

from hypothesis_faker import abas
from hypothesis_faker import addresses
from hypothesis_faker import android_platform_tokens
from hypothesis_faker import ascii_company_emails
from hypothesis_faker import ascii_emails
from hypothesis_faker import ascii_free_emails
from hypothesis_faker import ascii_safe_emails
from hypothesis_faker import bank_countries
from hypothesis_faker import bbans
from hypothesis_faker import building_numbers
from hypothesis_faker import chromes
from hypothesis_faker import cities
from hypothesis_faker import city_suffixes
from hypothesis_faker import company_emails
from hypothesis_faker import coordinates
from hypothesis_faker import countries
from hypothesis_faker import country_codes
from hypothesis_faker import current_countries
from hypothesis_faker import current_country_codes
from hypothesis_faker import dgas
from hypothesis_faker import domain_names
from hypothesis_faker import domain_words
from hypothesis_faker import ean8s
from hypothesis_faker import ean13s
from hypothesis_faker import eans
from hypothesis_faker import emails
from hypothesis_faker import firefoxes
from hypothesis_faker import free_email_domains
from hypothesis_faker import free_emails
from hypothesis_faker import hostnames
from hypothesis_faker import http_methods
from hypothesis_faker import iana_ids
from hypothesis_faker import ibans
from hypothesis_faker import image_urls
from hypothesis_faker import internet_explorers
from hypothesis_faker import ios_platform_tokens
from hypothesis_faker import ipv4_network_classes
from hypothesis_faker import ipv4_privates
from hypothesis_faker import ipv4_publics
from hypothesis_faker import ipv4s
from hypothesis_faker import ipv6s
from hypothesis_faker import license_plates
from hypothesis_faker import linux_platform_tokens
from hypothesis_faker import linux_processors
from hypothesis_faker import localized_ean8s
from hypothesis_faker import localized_ean13s
from hypothesis_faker import localized_eans
from hypothesis_faker import mac_addresses
from hypothesis_faker import mac_platform_tokens
from hypothesis_faker import mac_processors
from hypothesis_faker import nic_handle_lists
from hypothesis_faker import nic_handles
from hypothesis_faker import operas
from hypothesis_faker import port_numbers
from hypothesis_faker import postcodes
from hypothesis_faker import ripe_ids
from hypothesis_faker import safaris
from hypothesis_faker import safe_domain_names
from hypothesis_faker import safe_emails
from hypothesis_faker import slugs
from hypothesis_faker import street_addresses
from hypothesis_faker import street_names
from hypothesis_faker import street_suffixes
from hypothesis_faker import swift8s
from hypothesis_faker import swift11s
from hypothesis_faker import swifts
from hypothesis_faker import tlds
from hypothesis_faker import uri_extensions
from hypothesis_faker import uri_pages
from hypothesis_faker import uri_paths
from hypothesis_faker import uris
from hypothesis_faker import urls
from hypothesis_faker import user_agents
from hypothesis_faker import user_names
from hypothesis_faker import windows_platform_tokens
from hypothesis_faker.strategies import color_names
from hypothesis_faker.strategies import colors
from hypothesis_faker.strategies import hex_colors
from hypothesis_faker.strategies import rgb_colors
from hypothesis_faker.strategies import safe_color_names
from tests.utilities import env


@given(data=data())
@mark.parametrize(
    ["strategy", "type"],
    [
        # address #############################################################
        param(addresses, str),
        param(building_numbers, str),
        param(cities, str),
        param(city_suffixes, str),
        param(countries, str),
        param(country_codes, str),
        param(current_countries, str),
        param(current_country_codes, str),
        param(postcodes, str),
        param(street_addresses, str),
        param(street_names, str),
        param(street_suffixes, str),
        # automotive ##########################################################
        param(license_plates, str),
        # bank ################################################################
        param(abas, str),
        param(bank_countries, str),
        param(bbans, str),
        param(ibans, str),
        param(swifts, str),
        param(swift11s, str),
        param(swift8s, str),
        # barcode #############################################################
        param(eans, str),
        param(ean13s, str),
        param(ean8s, str),
        param(localized_eans, str),
        param(localized_ean13s, str),
        param(localized_ean8s, str),
        # color ###############################################################
        param(colors, str),
        param(color_names, str),
        param(hex_colors, str),
        param(rgb_colors, str),
        param(rgb_colors, str),
        param(safe_color_names, str),
        # geo #################################################################
        param(coordinates, Decimal),
        # internet ############################################################
        param(ascii_company_emails, str),
        param(ascii_emails, str),
        param(ascii_free_emails, str),
        param(ascii_safe_emails, str),
        param(company_emails, str),
        param(dgas, str),
        param(domain_names, str),
        param(domain_words, str),
        param(emails, str),
        param(free_emails, str),
        param(free_email_domains, str),
        param(hostnames, str),
        param(http_methods, str),
        param(iana_ids, str),
        param(image_urls, str),
        param(ipv4s, str),
        param(ipv4_network_classes, str),
        param(ipv4_privates, str),
        param(ipv4_publics, str),
        param(ipv6s, str),
        param(mac_addresses, str),
        param(nic_handles, str),
        param(
            nic_handle_lists,
            list,
            marks=mark.xfail(reason="List hashing not sorted yet"),
        ),
        param(port_numbers, int),
        param(ripe_ids, str),
        param(safe_domain_names, str),
        param(safe_emails, str),
        param(slugs, str),
        param(tlds, str),
        param(uris, str),
        param(uri_extensions, str),
        param(uri_pages, str),
        param(uri_paths, str),
        param(urls, str),
        param(user_names, str),
        # user_agent ##########################################################
        param(android_platform_tokens, str),
        param(chromes, str),
        param(firefoxes, str),
        param(internet_explorers, str),
        param(ios_platform_tokens, str),
        param(linux_platform_tokens, str),
        param(linux_processors, str),
        param(mac_platform_tokens, str),
        param(mac_processors, str),
        param(operas, str),
        param(safaris, str),
        param(user_agents, str),
        param(windows_platform_tokens, str),
    ],
)
def test_strategies(
    data: DataObject, strategy: Callable[..., SearchStrategy[Any]], type: type
) -> None:
    with env():
        assert isinstance(data.draw(strategy()), type)
