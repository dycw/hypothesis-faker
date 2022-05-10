from hypothesis_faker.strategies import abas
from hypothesis_faker.strategies import addresses
from hypothesis_faker.strategies import android_platform_tokens
from hypothesis_faker.strategies import ascii_company_emails
from hypothesis_faker.strategies import ascii_emails
from hypothesis_faker.strategies import ascii_free_emails
from hypothesis_faker.strategies import ascii_safe_emails
from hypothesis_faker.strategies import bank_countries
from hypothesis_faker.strategies import bbans
from hypothesis_faker.strategies import building_numbers
from hypothesis_faker.strategies import chromes
from hypothesis_faker.strategies import cities
from hypothesis_faker.strategies import city_suffixes
from hypothesis_faker.strategies import company_emails
from hypothesis_faker.strategies import coordinates
from hypothesis_faker.strategies import countries
from hypothesis_faker.strategies import country_codes
from hypothesis_faker.strategies import current_countries
from hypothesis_faker.strategies import current_country_codes
from hypothesis_faker.strategies import dgas
from hypothesis_faker.strategies import domain_names
from hypothesis_faker.strategies import domain_words
from hypothesis_faker.strategies import ean8s
from hypothesis_faker.strategies import ean13s
from hypothesis_faker.strategies import eans
from hypothesis_faker.strategies import emails
from hypothesis_faker.strategies import firefoxes
from hypothesis_faker.strategies import free_email_domains
from hypothesis_faker.strategies import free_emails
from hypothesis_faker.strategies import hostnames
from hypothesis_faker.strategies import http_methods
from hypothesis_faker.strategies import iana_ids
from hypothesis_faker.strategies import ibans
from hypothesis_faker.strategies import image_urls
from hypothesis_faker.strategies import internet_explorers
from hypothesis_faker.strategies import ios_platform_tokens
from hypothesis_faker.strategies import ipv4_network_classes
from hypothesis_faker.strategies import ipv4_privates
from hypothesis_faker.strategies import ipv4_publics
from hypothesis_faker.strategies import ipv4s
from hypothesis_faker.strategies import ipv6s
from hypothesis_faker.strategies import license_plates
from hypothesis_faker.strategies import linux_platform_tokens
from hypothesis_faker.strategies import linux_processors
from hypothesis_faker.strategies import localized_ean8s
from hypothesis_faker.strategies import localized_ean13s
from hypothesis_faker.strategies import localized_eans
from hypothesis_faker.strategies import mac_addresses
from hypothesis_faker.strategies import mac_platform_tokens
from hypothesis_faker.strategies import mac_processors
from hypothesis_faker.strategies import nic_handle_lists
from hypothesis_faker.strategies import nic_handles
from hypothesis_faker.strategies import operas
from hypothesis_faker.strategies import port_numbers
from hypothesis_faker.strategies import postcodes
from hypothesis_faker.strategies import ripe_ids
from hypothesis_faker.strategies import safaris
from hypothesis_faker.strategies import safe_domain_names
from hypothesis_faker.strategies import safe_emails
from hypothesis_faker.strategies import slugs
from hypothesis_faker.strategies import street_addresses
from hypothesis_faker.strategies import street_names
from hypothesis_faker.strategies import street_suffixes
from hypothesis_faker.strategies import swift8s
from hypothesis_faker.strategies import swift11s
from hypothesis_faker.strategies import swifts
from hypothesis_faker.strategies import tlds
from hypothesis_faker.strategies import uri_extensions
from hypothesis_faker.strategies import uri_pages
from hypothesis_faker.strategies import uri_paths
from hypothesis_faker.strategies import uris
from hypothesis_faker.strategies import urls
from hypothesis_faker.strategies import user_agents
from hypothesis_faker.strategies import user_names
from hypothesis_faker.strategies import windows_platform_tokens


__all__ = [
    # address #################################################################
    "addresses",
    "building_numbers",
    "cities",
    "city_suffixes",
    "coordinates",
    "countries",
    "country_codes",
    "current_countries",
    "current_country_codes",
    "postcodes",
    "street_addresses",
    "street_names",
    "street_suffixes",
    # automotive ##############################################################
    "license_plates",
    # bank ####################################################################
    "abas",
    "bank_countries",
    "bbans",
    "ibans",
    "swifts",
    "swift11s",
    "swift8s",
    # barcode #################################################################
    "eans",
    "ean13s",
    "ean8s",
    "localized_eans",
    "localized_ean13s",
    "localized_ean8s",
    # geo #####################################################################
    "coordinates",
    # internet ################################################################
    "ascii_company_emails",
    "ascii_emails",
    "ascii_free_emails",
    "ascii_safe_emails",
    "company_emails",
    "dgas",
    "domain_names",
    "domain_words",
    "emails",
    "free_emails",
    "free_email_domains",
    "hostnames",
    "http_methods",
    "iana_ids",
    "image_urls",
    "ipv4s",
    "ipv4_network_classes",
    "ipv4_privates",
    "ipv4_publics",
    "ipv6s",
    "mac_addresses",
    "nic_handles",
    "nic_handle_lists",
    "port_numbers",
    "ripe_ids",
    "safe_domain_names",
    "safe_emails",
    "slugs",
    "tlds",
    "uris",
    "uri_extensions",
    "uri_pages",
    "uri_paths",
    "urls",
    "user_names",
    # user_agent ##############################################################
    "android_platform_tokens",
    "chromes",
    "firefoxes",
    "internet_explorers",
    "ios_platform_tokens",
    "linux_platform_tokens",
    "linux_processors",
    "mac_platform_tokens",
    "mac_processors",
    "operas",
    "safaris",
    "user_agents",
    "windows_platform_tokens",
]
__version__ = "0.1.6"
