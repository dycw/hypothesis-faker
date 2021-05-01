from hypothesis import given
from hypothesis.strategies import DataObject
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import data
from hypothesis.strategies import integers
from hypothesis.strategies import none
from hypothesis.strategies import sampled_from
from hypothesis.strategies import tuples
from pytest import mark

from hypothesis_faker.providers.color import _COLOR_FORMAT
from hypothesis_faker.providers.color import _HUE
from hypothesis_faker.providers.color import _LUMINOSITY
from hypothesis_faker.providers.color import color_names
from hypothesis_faker.providers.color import colors
from hypothesis_faker.providers.color import hex_colors
from hypothesis_faker.providers.color import rgb_colors
from hypothesis_faker.providers.color import rgb_css_colors
from hypothesis_faker.providers.color import safe_color_names
from hypothesis_faker.providers.color import safe_hex_colors


@mark.parametrize(
    "strategy",
    [
        color_names,
        safe_color_names,
        hex_colors,
        safe_hex_colors,
        rgb_colors,
        rgb_css_colors,
    ],
)
@given(data=data())
def test_color_strategies(
    data: DataObject, strategy: SearchStrategy[str]
) -> None:
    assert isinstance(data.draw(strategy), str)


@given(
    data=data(),
    hue=none()
    | integers(0, 360)
    | tuples(integers(0, 360), integers(0, 360))
    | sampled_from(
        [
            "monochrome",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "purple",
            "pink",
        ]
    ),
    luminosity=none() | sampled_from(["bright", "dark", "light", "random"]),
    color_format=sampled_from(["hsv", "hsl", "rgb", "hex"]),
)
def test_colors(
    data: DataObject,
    hue: _HUE,
    luminosity: _LUMINOSITY,
    color_format: _COLOR_FORMAT,
) -> None:
    assert isinstance(data.draw(colors(hue, luminosity, color_format)), str)
