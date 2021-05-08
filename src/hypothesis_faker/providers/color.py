from __future__ import annotations

from math import ceil
from math import floor
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Union

from faker.providers.color import Provider as ColorProvider
from faker.providers.color.color import RandomColor
from hypothesis.errors import InvalidArgument
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import composite
from hypothesis.strategies import integers
from hypothesis.strategies import just
from hypothesis.strategies import lists
from hypothesis.strategies import sampled_from

from hypothesis_faker.types import T


color_names = sampled_from(list(ColorProvider.all_colors))
safe_color_names = sampled_from(ColorProvider.safe_colors)
hex_colors = integers(1, 16777215).map(lambda n: f"#{n:06x}")
safe_hex_colors = lists(integers(0, 15), min_size=3, max_size=3).map(
    lambda ints: "#{}".format("".join(f"{17*i:02x}" for i in ints))
)
rgb_colors = lists(integers(0, 255), min_size=3, max_size=3).map(
    lambda ints: ",".join(map(str, ints))
)
rgb_css_colors = lists(integers(0, 255), min_size=3, max_size=3).map(
    lambda ints: "rgb({})".format(",".join(map(str, ints)))
)


# colors


_RANDOM_COLOR = RandomColor()
_HUE = Optional[
    Union[
        int,
        Sequence[Tuple[int, int]],
        Literal[
            "monochrome",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "purple",
            "pink",
        ],
    ]
]
_LUMINOSITY = Optional[Literal["bright", "dark", "light", "random"]]
_COLOR_FORMAT = Literal["hsv", "hsl", "rgb", "hex"]


def colors(
    hue: _HUE = None,
    luminosity: _LUMINOSITY = None,
    color_format: _COLOR_FORMAT = "hex",
) -> SearchStrategy[str]:
    if isinstance(hue, int):
        if not (0 <= hue <= 360):
            raise InvalidArgument(
                f"{hue=} is an int, and thus must lie in [0, 360]"
            )
    elif isinstance(hue, Sequence) and not isinstance(hue, str):
        if not (
            len(hue) == 2
            and all(isinstance(h, int) and 0 <= h <= 360 for h in hue)
        ):
            raise InvalidArgument(
                f"{hue=} is a sequence, and thus must be a pairs of ints in "
                "[0, 360]"
            )
    else:
        pass

    @composite
    def inner(draw: Callable[[SearchStrategy[T]], T]) -> str:
        h = draw(_hues(hue))
        s = draw(_saturations(h, hue, luminosity))
        b = draw(_brightnesses(h, s, luminosity))
        return _RANDOM_COLOR.set_format([h, s, b], color_format)

    return inner()


def _hues(hue: _HUE) -> SearchStrategy[int]:
    min_value, max_value = _RANDOM_COLOR.get_hue_range(hue)

    def f(n: int) -> int:
        return n if n >= 0 else (n + 360)

    return integers(min_value, max_value).map(f)


def _saturations(
    hue: int, hue_name: _HUE, luminosity: _LUMINOSITY
) -> SearchStrategy[int]:
    if luminosity == "random":
        return integers(0, 100)
    elif hue_name == "monochrome":
        return just(0)
    else:
        s_min, s_max = _RANDOM_COLOR.get_saturation_range(hue)
        if luminosity == "bright":
            s_min = 55
        elif luminosity == "dark":
            s_min = s_max - 10
        elif luminosity == "light":
            s_max = 55
        return integers(s_min, s_max)


def _brightnesses(
    h: int, s: int, luminosity: _LUMINOSITY
) -> SearchStrategy[int]:
    b_min = _RANDOM_COLOR.get_minimum_brightness(h, s)
    b_max = 100
    if luminosity == "dark":
        b_max = b_min + 20
    elif luminosity == "light":
        b_min = (b_max + b_min) / 2
    elif luminosity == "random":
        b_min = 0
        b_max = 100
    return integers(ceil(b_min), floor(b_max))
