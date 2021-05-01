from hypothesis import given
from hypothesis.strategies import DataObject
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import data
from pytest import mark

from hypothesis_faker.providers.color import color_names
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
