from __future__ import annotations

from itertools import chain
from typing import Callable

from faker.providers.lorem import Provider as LoremProvider
from faker.providers.lorem.en_US import Provider as LoremProviderEnUS
from hypothesis.errors import InvalidArgument
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import composite
from hypothesis.strategies import lists
from hypothesis.strategies import sampled_from

from hypothesis_faker.types import T


_WORD_CONNECTOR = LoremProvider.word_connector


words = sampled_from(LoremProviderEnUS.word_list)
sentences = lists(words).map(
    lambda x: _join_words_into_sentence(x) if x else ""
)
paragraphs = lists(sentences).map(
    lambda x: _WORD_CONNECTOR.join(x) if x else ""
)


def texts(max_length: int = 200) -> SearchStrategy[str]:
    @composite
    def inner(draw: Callable[[SearchStrategy[T]], T]) -> str:
        parts = []
        if max_length < 5:
            raise InvalidArgument(f"{max_length=} must be at least 5")
        elif 5 <= max_length < 25:
            while sum(map(len, parts)) < max_length:
                parts.append(draw(words))
            return _join_words_into_sentence(parts)
        else:
            if 25 <= max_length < 100:
                raw_strategy = sentences
                sep = _WORD_CONNECTOR
            else:
                raw_strategy = paragraphs
                sep = "\n"
            strategy = raw_strategy.filter(bool)
            while sum(map(len, parts)) < max_length:
                parts.append(draw(strategy))
            return sep.join(parts)

    return inner()


def _join_words_into_sentence(words: list[str]) -> str:
    first, *rest = words
    return (
        _WORD_CONNECTOR.join(chain([first.title()], rest))
        + LoremProvider.sentence_punctuation
    )
