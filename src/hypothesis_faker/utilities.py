from bisect import bisect
from typing import Any
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


class WeightedList(list[tuple[T, Num]]):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
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

    def __getitem__(self, item: Num) -> T:
        if not 0.0 <= item < self.total_weight:
            raise IndexError(f"Invalid {item=}")
        return self._elements[bisect(self._cum_weights, item)]


@composite
def weighted_samples(
    draw: Callable[[SearchStrategy[T]], T], items: list[tuple[U, Num]]
) -> U:
    if isinstance(items, WeightedList):
        wlist = items
    else:
        wlist = WeightedList(items)
    i = draw(floats(0.0, wlist.total_weight, exclude_max=True))
    return wlist[i]
