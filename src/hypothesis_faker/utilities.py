from bisect import bisect
from functools import reduce
from re import sub
from typing import Iterable
from typing import cast

from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import floats

from hypothesis_faker.types import Num
from hypothesis_faker.types import T


def fill_format_string(format_: str, replacements: dict[str, str]) -> str:
    return reduce(_fill_format_1, replacements.items(), format_)


def _fill_format_1(format_: str, pair: tuple[str, str]) -> str:
    token, replacement = pair
    return sub(f"{{{{{token}}}}}", replacement, format_)


class WeightedList(list[tuple[T, Num]]):
    def __init__(self, items: Iterable[tuple[T, Num]]) -> None:
        super().__init__(items)
        if not self:
            raise ValueError(f"{self} cannot be empty")
        try:
            elements, weights = zip(*self)
        except TypeError:
            raise TypeError(f"{self} could not be zipped into 2 lists")
        self._elements = cast(list[T], list(elements))
        self._weights = cast(list[Num], list(weights))
        self.total_weight, self._cum_weights = 0.0, []
        for weight in self._weights:
            if weight < 0.0:
                raise ValueError(f"Invalid {weight=}")
            self.total_weight += weight
            self._cum_weights.append(self.total_weight)

    def __add__(self, other: "WeightedList[T]") -> "WeightedList[T]":
        return WeightedList(super().__add__(other))

    def __getitem__(self, item: Num) -> T:
        if not 0.0 <= item < self.total_weight:
            raise IndexError(f"Invalid {item=}")
        return self._elements[bisect(self._cum_weights, item)]


def weighted_samples(wlist: WeightedList[T]) -> SearchStrategy[T]:
    def inner(i: float) -> T:
        return wlist[i]

    return floats(0.0, wlist.total_weight, exclude_max=True).map(inner)
