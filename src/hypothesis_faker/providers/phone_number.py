from __future__ import annotations

from faker.providers.phone_number import Provider as PhoneNumberProvider
from faker.providers.phone_number.en_US import (
    Provider as PhoneNumberProviderEnUS,
)
from hypothesis.strategies import sampled_from

from hypothesis_faker.utilities import numerified


phone_numbers = sampled_from(PhoneNumberProviderEnUS.formats).flatmap(
    numerified
)
country_calling_codes = sampled_from(PhoneNumberProvider.country_calling_codes)
msisdns = sampled_from(PhoneNumberProvider.msisdn_formats).flatmap(numerified)
