from hypothesis.strategies import SearchStrategy

from hypothesis_faker.providers import Provider


def addresses() -> SearchStrategy[str]:
    return Provider.address.get_strategy()
