from bisect import bisect
from collections.abc import Sequence
from typing import Callable
from typing import TypeVar
from typing import Union
from typing import cast

from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import composite
from hypothesis.strategies import floats


Num = Union[int, float]
T = TypeVar("T")
U = TypeVar("U")


class WeightedList(Sequence[T]):
    def __init__(self, *items: tuple[T, Num]) -> None:
        if not items:
            raise ValueError(f"{items=} cannot be empty")
        elements, weights = zip(*items)
        self._elements = cast(list[T], list(elements))
        self._weights = cast(list[Num], list(weights))
        self.total_weight, self._cum_weights = 0.0, []
        for weight in self._weights:
            if weight < 0.0:
                raise ValueError(f"Invalid {weight=}")
            self.total_weight += weight
            self._cum_weights.append(self.total_weight)

    def __len__(self) -> int:
        return len(self._elements)

    def __getitem__(self, item: Num) -> T:
        if not 0.0 <= item < self.total_weight:
            raise IndexError(f"Invalid {item=}")
        return self._elements[bisect(self._cum_weights, item)]


@composite
def weighted_samples(
    draw: Callable[[SearchStrategy[T]], T], *items: tuple[U, Num]
) -> U:
    wlist = WeightedList(*items)
    i = draw(floats(0.0, wlist.total_weight, exclude_max=True))
    return wlist[i]
