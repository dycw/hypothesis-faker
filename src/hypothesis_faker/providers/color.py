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
    @composite
    def inner(draw: Callable[[SearchStrategy[T]], T]) -> int:
        min_value, max_value = _RANDOM_COLOR.get_hue_range(hue)
        drawn = draw(integers(min_value, max_value))
        if drawn < 0:
            drawn += 360
        return drawn

    return inner()


def _saturations(
    hue: int, hue_name: _HUE, luminosity: _LUMINOSITY
) -> SearchStrategy[int]:
    @composite
    def inner(draw: Callable[[SearchStrategy[T]], T]) -> int:
        if luminosity == "random":
            return draw(integers(0, 100))
        elif hue_name == "monochrome":
            return 0
        else:
            s_min, s_max = _RANDOM_COLOR.get_saturation_range(hue)
            if luminosity == "bright":
                s_min = 55
            elif luminosity == "dark":
                s_min = s_max - 10
            elif luminosity == "light":
                s_max = 55
            return draw(integers(s_min, s_max))

    return inner()


def _brightnesses(
    h: int, s: int, luminosity: _LUMINOSITY
) -> SearchStrategy[int]:
    @composite
    def inner(draw: Callable[[SearchStrategy[T]], T]) -> int:
        b_min = _RANDOM_COLOR.get_minimum_brightness(h, s)
        b_max = 100
        if luminosity == "dark":
            b_max = b_min + 20
        elif luminosity == "light":
            b_min = (b_max + b_min) / 2
        elif luminosity == "random":
            b_min = 0
            b_max = 100
        return draw(integers(ceil(b_min), floor(b_max)))

    return inner()
