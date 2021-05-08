import datetime as dt
from datetime import tzinfo
from typing import Callable
from typing import Optional

from hypothesis import given
from hypothesis.strategies import DataObject
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import data
from hypothesis.strategies import datetimes
from hypothesis.strategies import just
from hypothesis.strategies import none
from pytest import mark
from pytz import UTC

from hypothesis_faker.providers.date_time import am_pms
from hypothesis_faker.providers.date_time import date_times
from hypothesis_faker.providers.date_time import date_times_ad


@given(am_pm=am_pms)
def test_am_pms(am_pm: str) -> None:
    assert am_pm in {"AM", "PM"}


@mark.parametrize(
    ["strategy", "min_value"],
    [
        (date_times, dt.datetime(1970, 1, 1)),
        (date_times_ad, dt.datetime(1, 1, 1)),
    ],
)
@given(data=data())
def test_date_times(
    strategy: Callable[
        [Optional[tzinfo], Optional[dt.datetime]], SearchStrategy[dt.datetime]
    ],
    min_value: dt.datetime,
    data: DataObject,
) -> None:
    tzinfo = data.draw(just(UTC) | none())
    end_datetime = data.draw(datetimes(min_value=min_value) | none())
    datetime = data.draw(strategy(tzinfo, end_datetime))
    assert isinstance(datetime, dt.datetime)
    assert (
        min_value.replace(tzinfo=tzinfo)
        <= datetime
        <= (
            dt.datetime.now(tz=tzinfo)
            if end_datetime is None
            else end_datetime.replace(tzinfo=tzinfo)
        )
    )
    assert datetime.tzinfo is tzinfo
