from hypothesis import given
from hypothesis.strategies import DataObject
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import data
from pytest import mark

from hypothesis_faker.providers.lorem import sentences
from hypothesis_faker.providers.lorem import words


@mark.parametrize("strategy", [words, sentences])
@given(data=data())
def test_words(data: DataObject, strategy: SearchStrategy[str]) -> None:
    assert isinstance(data.draw(strategy), str)
