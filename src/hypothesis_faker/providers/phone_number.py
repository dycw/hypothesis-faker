from faker.providers.phone_number import Provider as PhoneNumberProvider
from faker.providers.phone_number.en_US import (
    Provider as PhoneNumberProviderEnUS,
)
from hypothesis.strategies import sampled_from

from hypothesis_faker.utilities import numerified


_COUNTRY_CALLING_CODES = PhoneNumberProvider.country_calling_codes
_MSISDN_FORMATS = PhoneNumberProvider.msisdn_formats
_FORMATS = PhoneNumberProviderEnUS.formats


phone_numbers = sampled_from(_FORMATS).flatmap(numerified)
country_calling_codes = sampled_from(_COUNTRY_CALLING_CODES)
msisdns = sampled_from(_MSISDN_FORMATS).flatmap(numerified)
