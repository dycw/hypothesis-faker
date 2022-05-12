import datetime as dt
from decimal import Decimal
from typing import Any
from typing import Callable
from uuid import UUID

from hypothesis import given
from hypothesis.strategies import DataObject
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import data
from pytest import mark
from pytest import param

from hypothesis_faker import abas
from hypothesis_faker import addresses
from hypothesis_faker import am_pms
from hypothesis_faker import android_platform_tokens
from hypothesis_faker import ascii_company_emails
from hypothesis_faker import ascii_emails
from hypothesis_faker import ascii_free_emails
from hypothesis_faker import ascii_safe_emails
from hypothesis_faker import bank_countries
from hypothesis_faker import bbans
from hypothesis_faker import binaries
from hypothesis_faker import booleans
from hypothesis_faker import bss
from hypothesis_faker import building_numbers
from hypothesis_faker import catch_phrases
from hypothesis_faker import centuries
from hypothesis_faker import chromes
from hypothesis_faker import cities
from hypothesis_faker import city_suffixes
from hypothesis_faker import color_names
from hypothesis_faker import colors
from hypothesis_faker import companies
from hypothesis_faker import company_emails
from hypothesis_faker import company_suffixes
from hypothesis_faker import coordinates
from hypothesis_faker import countries
from hypothesis_faker import country_calling_codes
from hypothesis_faker import country_codes
from hypothesis_faker import credit_card_expires
from hypothesis_faker import credit_card_numbers
from hypothesis_faker import credit_card_providers
from hypothesis_faker import credit_card_security_codes
from hypothesis_faker import credit_cards_full
from hypothesis_faker import cryptocurrencies
from hypothesis_faker import cryptocurrency_codes
from hypothesis_faker import cryptocurrency_names
from hypothesis_faker import csvs
from hypothesis_faker import currencies
from hypothesis_faker import currency_codes
from hypothesis_faker import currency_names
from hypothesis_faker import currency_symbols
from hypothesis_faker import current_countries
from hypothesis_faker import current_country_codes
from hypothesis_faker import date_between_dates
from hypothesis_faker import date_objects
from hypothesis_faker import date_time
from hypothesis_faker import date_times_ad
from hypothesis_faker import date_times_between
from hypothesis_faker import date_times_between_dates
from hypothesis_faker import date_times_this_century
from hypothesis_faker import date_times_this_decade
from hypothesis_faker import date_times_this_month
from hypothesis_faker import date_times_this_year
from hypothesis_faker import dates
from hypothesis_faker import dates_between
from hypothesis_faker import dates_of_birth
from hypothesis_faker import dates_this_century
from hypothesis_faker import dates_this_decade
from hypothesis_faker import dates_this_month
from hypothesis_faker import dates_this_year
from hypothesis_faker import days_of_month
from hypothesis_faker import days_of_week
from hypothesis_faker import dgas
from hypothesis_faker import domain_names
from hypothesis_faker import domain_words
from hypothesis_faker import dsvs
from hypothesis_faker import ean8s
from hypothesis_faker import ean13s
from hypothesis_faker import eans
from hypothesis_faker import emails
from hypothesis_faker import file_extensions
from hypothesis_faker import file_names
from hypothesis_faker import file_paths
from hypothesis_faker import firefoxes
from hypothesis_faker import first_name_females
from hypothesis_faker import first_name_males
from hypothesis_faker import first_name_nonbinaries
from hypothesis_faker import first_names
from hypothesis_faker import fixed_widths
from hypothesis_faker import free_email_domains
from hypothesis_faker import free_emails
from hypothesis_faker import future_dates
from hypothesis_faker import future_datetimes
from hypothesis_faker import hex_colors
from hypothesis_faker import hostnames
from hypothesis_faker import http_methods
from hypothesis_faker import iana_ids
from hypothesis_faker import ibans
from hypothesis_faker import image_urls
from hypothesis_faker import images
from hypothesis_faker import internet_explorers
from hypothesis_faker import ios_platform_tokens
from hypothesis_faker import ipv4_network_classes
from hypothesis_faker import ipv4_privates
from hypothesis_faker import ipv4_publics
from hypothesis_faker import ipv4s
from hypothesis_faker import ipv6s
from hypothesis_faker import isbn10s
from hypothesis_faker import isbn13s
from hypothesis_faker import iso8601s
from hypothesis_faker import jobs
from hypothesis_faker import jsons
from hypothesis_faker import language_names
from hypothesis_faker import last_name_females
from hypothesis_faker import last_name_males
from hypothesis_faker import last_name_nonbinaries
from hypothesis_faker import last_names
from hypothesis_faker import license_plates
from hypothesis_faker import linux_platform_tokens
from hypothesis_faker import linux_processors
from hypothesis_faker import localized_ean8s
from hypothesis_faker import localized_ean13s
from hypothesis_faker import localized_eans
from hypothesis_faker import mac_addresses
from hypothesis_faker import mac_platform_tokens
from hypothesis_faker import mac_processors
from hypothesis_faker import md5s
from hypothesis_faker import mime_types
from hypothesis_faker import month_names
from hypothesis_faker import months
from hypothesis_faker import msisdns
from hypothesis_faker import name_females
from hypothesis_faker import name_males
from hypothesis_faker import name_nonbinaries
from hypothesis_faker import names
from hypothesis_faker import nic_handle_lists
from hypothesis_faker import nic_handles
from hypothesis_faker import null_booleans
from hypothesis_faker import operas
from hypothesis_faker import paragraph_lists
from hypothesis_faker import paragraphs
from hypothesis_faker import passwords
from hypothesis_faker import past_dates
from hypothesis_faker import past_datetime
from hypothesis_faker import phone_numbers
from hypothesis_faker import port_numbers
from hypothesis_faker import postcodes
from hypothesis_faker import prefix_females
from hypothesis_faker import prefix_males
from hypothesis_faker import prefix_nonbinaries
from hypothesis_faker import prefixes
from hypothesis_faker import pricetags
from hypothesis_faker import profiles
from hypothesis_faker import psvs
from hypothesis_faker import pytimezones
from hypothesis_faker import rgb_colors
from hypothesis_faker import rgb_css_colors
from hypothesis_faker import ripe_ids
from hypothesis_faker import safaris
from hypothesis_faker import safe_color_names
from hypothesis_faker import safe_domain_names
from hypothesis_faker import safe_emails
from hypothesis_faker import sentence_lists
from hypothesis_faker import sentences
from hypothesis_faker import sha1s
from hypothesis_faker import sha256s
from hypothesis_faker import simple_profiles
from hypothesis_faker import slugs
from hypothesis_faker import street_addresses
from hypothesis_faker import street_names
from hypothesis_faker import street_suffixes
from hypothesis_faker import suffix_females
from hypothesis_faker import suffix_males
from hypothesis_faker import suffix_nonbinaries
from hypothesis_faker import suffixes
from hypothesis_faker import swift8s
from hypothesis_faker import swift11s
from hypothesis_faker import swifts
from hypothesis_faker import tars
from hypothesis_faker import text_lists
from hypothesis_faker import texts
from hypothesis_faker import time_deltas
from hypothesis_faker import time_objects
from hypothesis_faker import time_series
from hypothesis_faker import times
from hypothesis_faker import timezones
from hypothesis_faker import tlds
from hypothesis_faker import tsvs
from hypothesis_faker import unix_devices
from hypothesis_faker import unix_partitions
from hypothesis_faker import unix_times
from hypothesis_faker import uri_extensions
from hypothesis_faker import uri_pages
from hypothesis_faker import uri_paths
from hypothesis_faker import uris
from hypothesis_faker import urls
from hypothesis_faker import user_agents
from hypothesis_faker import user_names
from hypothesis_faker import uuid4s
from hypothesis_faker import windows_platform_tokens
from hypothesis_faker import word_lists
from hypothesis_faker import words
from hypothesis_faker import years
from hypothesis_faker import zips
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
        param(rgb_css_colors, str),
        param(safe_color_names, str),
        # company #############################################################
        param(bss, str),
        param(catch_phrases, str),
        param(companies, str),
        param(company_suffixes, str),
        # credit card #########################################################
        param(credit_card_expires, str),
        param(credit_cards_full, str),
        param(credit_card_numbers, str),
        param(credit_card_providers, str),
        param(credit_card_security_codes, str),
        # currency ############################################################
        param(cryptocurrencies, tuple),
        param(cryptocurrency_codes, str),
        param(cryptocurrency_names, str),
        param(currencies, tuple),
        param(currency_codes, str),
        param(currency_names, str),
        param(currency_symbols, str),
        param(pricetags, str),
        # date_time ###########################################################
        param(am_pms, str),
        param(centuries, str),
        param(dates, str),
        param(dates_between, dt.date),
        param(date_between_dates, dt.date),
        param(date_objects, dt.date),
        param(dates_of_birth, dt.date),
        param(dates_this_century, dt.date),
        param(dates_this_decade, dt.date),
        param(dates_this_month, dt.date),
        param(dates_this_year, dt.date),
        param(date_time, dt.datetime),
        param(date_times_ad, dt.datetime),
        param(date_times_between, dt.datetime),
        param(date_times_between_dates, dt.datetime),
        param(date_times_this_century, dt.datetime),
        param(date_times_this_decade, dt.datetime),
        param(date_times_this_month, dt.datetime),
        param(date_times_this_year, dt.datetime),
        param(days_of_month, str),
        param(days_of_week, str),
        param(future_dates, dt.date),
        param(future_datetimes, dt.datetime),
        param(iso8601s, str),
        param(months, str),
        param(month_names, str),
        param(past_dates, dt.date),
        param(past_datetime, dt.datetime),
        param(
            pytimezones, (dt.tzinfo, None), marks=mark.xfail(reason="hashing")
        ),
        param(times, str),
        param(time_deltas, dt.timedelta),
        param(time_objects, dt.time),
        param(time_series, object, marks=mark.xfail(reason="pickle")),
        param(timezones, str),
        param(unix_times, int),
        param(years, str),
        # file ################################################################
        param(file_extensions, str),
        param(file_names, str),
        param(file_paths, str),
        param(mime_types, str),
        param(unix_devices, str),
        param(unix_partitions, str),
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
        param(nic_handle_lists, list, marks=mark.xfail(reason="hashing")),
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
        # isbn ################################################################
        param(isbn10s, str),
        param(isbn13s, str),
        # job #################################################################
        param(jobs, str),
        # lorem ###############################################################
        param(paragraphs, str),
        param(paragraph_lists, list, marks=mark.xfail(reason="hashing")),
        param(sentences, str),
        param(sentence_lists, list, marks=mark.xfail(reason="hashing")),
        param(texts, str),
        param(text_lists, list, marks=mark.xfail(reason="hashing")),
        param(words, str),
        param(word_lists, list, marks=mark.xfail(reason="hashing")),
        # misc ################################################################
        param(binaries, bytes),
        param(booleans, bool),
        param(csvs, str),
        param(dsvs, str),
        param(fixed_widths, str),
        param(images, bytes),
        param(jsons, str),
        param(md5s, (bytes, str)),
        param(null_booleans, (bool, type(None))),
        param(passwords, str),
        param(psvs, str),
        param(sha1s, (bytes, str)),
        param(sha256s, (bytes, str)),
        param(tars, bytes),
        param(tsvs, str),
        param(uuid4s, (bytes, str, UUID), marks=mark.xfail(reason="pickle")),
        param(zips, bytes),
        # person ##############################################################
        param(first_names, str),
        param(first_name_females, str),
        param(first_name_males, str),
        param(first_name_nonbinaries, str),
        param(language_names, str),
        param(last_names, str),
        param(last_name_females, str),
        param(last_name_males, str),
        param(last_name_nonbinaries, str),
        param(names, str),
        param(name_females, str),
        param(name_males, str),
        param(name_nonbinaries, str),
        param(prefixes, str),
        param(prefix_females, str),
        param(prefix_males, str),
        param(prefix_nonbinaries, str),
        param(suffixes, str),
        param(suffix_females, str),
        param(suffix_males, str),
        param(suffix_nonbinaries, str),
        # phone_number ########################################################
        param(country_calling_codes, str),
        param(msisdns, str),
        param(phone_numbers, str),
        # profile #############################################################
        param(profiles, dict, marks=mark.xfail(reason="hashing")),
        param(simple_profiles, dict, marks=mark.xfail(reason="hashing")),
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
