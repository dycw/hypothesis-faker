from typing import Callable

from faker.providers.color import Provider as ColorProvider
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import composite
from hypothesis.strategies import integers
from hypothesis.strategies import lists
from hypothesis.strategies import sampled_from

from hypothesis_faker.types import T


_ALL_COLORS = ColorProvider.all_colors
_SAFE_COLORS = ColorProvider.safe_colors


color_names = sampled_from(list(_ALL_COLORS))
safe_color_names = sampled_from(_SAFE_COLORS)


@composite
def _hex_colors(draw: Callable[[SearchStrategy[T]], T]) -> str:
    n = draw(integers(1, 16777215))
    return f"#{n:06x}"


hex_colors = _hex_colors()


@composite
def _safe_hex_colors(draw: Callable[[SearchStrategy[T]], T]) -> str:
    ints = draw(lists(integers(0, 15), min_size=3, max_size=3))
    parts = (f"{17*i:02x}" for i in ints)
    return "#{}".format("".join(parts))


safe_hex_colors = _safe_hex_colors()


@composite
def _rgb_colors(draw: Callable[[SearchStrategy[T]], T]) -> str:
    ints = draw(lists(integers(0, 255), min_size=3, max_size=3))
    return ",".join(str(i) for i in ints)


rgb_colors = _rgb_colors()


@composite
def _rgb_css_colors(draw: Callable[[SearchStrategy[T]], T]) -> str:
    ints = draw(lists(integers(0, 255), min_size=3, max_size=3))
    return "rgb({})".format(",".join(str(i) for i in ints))


rgb_css_colors = _rgb_css_colors()
