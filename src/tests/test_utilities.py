from hypothesis import given
from hypothesis.strategies import floats
from pytest import raises

from hypothesis_faker.utilities import WeightedList
from hypothesis_faker.utilities import weighted_samples


@given(i=floats(-1.0, 7.0, allow_nan=False, allow_infinity=False))
def test_weighted_list(i: float) -> None:
    wlist = WeightedList(("a", 3), ("b", 1), ("c", 2))
    assert len(wlist) == 3
    if 0 <= i < 3.0:
        assert wlist[i] == "a"
    elif 3.0 <= i < 4.0:
        assert wlist[i] == "b"
    elif 4.0 <= i < 6.0:
        assert wlist[i] == "c"
    else:
        with raises(IndexError):
            wlist[i]


@given(letter=weighted_samples(("a", 3), ("b", 1), ("c", 2)))
def test_weighted_samples(letter: str) -> None:
    assert letter in {"a", "b", "c"}