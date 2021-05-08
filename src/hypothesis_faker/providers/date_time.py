from __future__ import annotations

import datetime as dt
from datetime import tzinfo

from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import datetimes
from hypothesis.strategies import just
from hypothesis.strategies import sampled_from


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


am_pms = sampled_from(["AM", "PM"])


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
