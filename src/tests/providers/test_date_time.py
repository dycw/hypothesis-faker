from __future__ import annotations

import datetime as dt
from datetime import tzinfo
from typing import Callable

from hypothesis import assume
from hypothesis import given
from hypothesis.errors import InvalidArgument
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
from hypothesis_faker.providers.date_time import unix_times


@given(am_pm=am_pms)
def test_am_pms(am_pm: str) -> None:
    assert am_pm in {"AM", "PM"}


@given(
    data=data(),
    start_datetime=datetimes() | none(),
    end_datetime=datetimes() | none(),
)
def test_unix_times(
    data: DataObject,
    start_datetime: dt.datetime | None,
    end_datetime: dt.datetime | None,
) -> None:
    try:
        unix = data.draw(
            unix_times(start_datetime=start_datetime, end_datetime=end_datetime)
        )
    except InvalidArgument:
        assume(False)
    else:
        assert isinstance(unix, int)
        datetime = dt.datetime.fromtimestamp(unix, tz=UTC).replace(tzinfo=None)
        buffer = dt.timedelta(seconds=1)  # 1 second buffer needed
        assert (
            (
                (
                    dt.datetime(1970, 1, 1)
                    if start_datetime is None
                    else start_datetime
                )
                - buffer
            )
            <= datetime
            <= (
                (dt.datetime.now() if end_datetime is None else end_datetime)
                + buffer
            )
        )


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
        [tzinfo | None, dt.datetime | None], SearchStrategy[dt.datetime]
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
