from hypothesis import HealthCheck
from hypothesis import given
from hypothesis import settings
from hypothesis.strategies import DataObject
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import data
from hypothesis.strategies import integers
from pytest import mark

from hypothesis_faker.providers.lorem import paragraphs
from hypothesis_faker.providers.lorem import sentences
from hypothesis_faker.providers.lorem import texts
from hypothesis_faker.providers.lorem import words


@mark.parametrize("strategy", [words, sentences, paragraphs])
@given(data=data())
def test_words_sentences_and_paragraphs(
    data: DataObject, strategy: SearchStrategy[str]
) -> None:
    assert isinstance(data.draw(strategy), str)


@given(max_length=integers(5, 300), data=data())
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_texts(max_length: int, data: DataObject) -> None:
    assert isinstance(data.draw(texts(max_length)), str)
