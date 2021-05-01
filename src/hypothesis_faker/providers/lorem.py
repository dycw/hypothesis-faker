from typing import Callable

from faker.providers.lorem import Provider as LoremProvider
from faker.providers.lorem.en_US import Provider as LoremProviderEnUS
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import composite
from hypothesis.strategies import lists
from hypothesis.strategies import sampled_from

from hypothesis_faker.types import T


_WORD_LIST = LoremProviderEnUS.word_list
_WORD_CONNECTOR = LoremProvider.word_connector
_SENTENCE_PUNCTUATION = LoremProvider.sentence_punctuation


words = sampled_from(_WORD_LIST)


@composite
def _sentences(draw: Callable[[SearchStrategy[T]], T]) -> str:
    drawn_words = draw(lists(words))
    return _WORD_CONNECTOR.join(drawn_words) + _SENTENCE_PUNCTUATION


sentences = _sentences()
