from __future__ import annotations

import datetime as dt
from datetime import tzinfo

from faker.providers.date_time import datetime_to_timestamp
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import datetimes
from hypothesis.strategies import just
from hypothesis.strategies import sampled_from


def unix_times(
    end_datetime: dt.datetime | None = None,
    start_datetime: dt.datetime | None = None,
) -> SearchStrategy[int]:
    return datetimes(
        min_value=dt.datetime(1970, 1, 1)
        if start_datetime is None
        else start_datetime,
        max_value=dt.datetime.now() if end_datetime is None else end_datetime,
    ).map(datetime_to_timestamp)


def date_times(
    tzinfo: tzinfo | None = None, end_datetime: dt.datetime | None = None
) -> SearchStrategy[dt.datetime]:
    return _date_times_between(
        tzinfo=tzinfo,
        end_datetime=end_datetime,
        min_value=dt.datetime(1970, 1, 1),
    )


def date_times_ad(
    tzinfo: tzinfo | None = None, end_datetime: dt.datetime | None = None
) -> SearchStrategy[dt.datetime]:
    return _date_times_between(
        tzinfo=tzinfo, end_datetime=end_datetime, min_value=dt.datetime(1, 1, 1)
    )


def _date_times_between(
    tzinfo: tzinfo | None = None,
    end_datetime: dt.datetime | None = None,
    *,
    min_value: dt.datetime,
) -> SearchStrategy[dt.datetime]:
    return datetimes(
        min_value=min_value,
        max_value=dt.datetime.now() if end_datetime is None else end_datetime,
        timezones=just(tzinfo),
    )


def iso8601s(
    tzinfo: tzinfo | None = None, end_datetime: dt.datetime | None = None
) -> SearchStrategy[str]:
    return date_times(tzinfo=tzinfo, end_datetime=end_datetime).map(
        lambda dt: dt.isoformat()
    )


def dates(
    pattern: str = "%Y-%m-%d", end_datetime: dt.datetime | None = None
) -> SearchStrategy[str]:
    return date_times(end_datetime=end_datetime).map(
        lambda dt: dt.strftime(pattern)
    )


def date_objects(
    end_datetime: dt.datetime | None = None,
) -> SearchStrategy[dt.date]:
    return date_times(end_datetime=end_datetime).map(lambda dt: dt.date())


def times(pattern: str = "%H:%M:%S") -> SearchStrategy[str]:
    return date_times().map(lambda dt: dt.time().strftime(pattern))


time_objects = date_times().map(lambda dt: dt.time())
am_pms = sampled_from(["AM", "PM"])
