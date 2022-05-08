from contextlib import contextmanager
from tempfile import TemporaryDirectory
from typing import Any
from typing import Dict
from typing import Iterator
from typing import Optional

from tempenv import TemporaryEnvironment

from hypothesis_faker.settings import HYPOTHESIS_FAKER_DURATION
from hypothesis_faker.settings import HYPOTHESIS_FAKER_MAX_ITEMS
from hypothesis_faker.settings import HYPOTHESIS_FAKER_ROOT
from hypothesis_faker.settings import HYPOTHESIS_FAKER_UPDATE_FREQ


@contextmanager
def env(env: Optional[Dict[str, Any]] = None) -> Iterator[None]:
    with TemporaryDirectory() as temp_dir:
        base: Dict[str, Optional[str]] = {
            HYPOTHESIS_FAKER_ROOT: temp_dir,
            HYPOTHESIS_FAKER_UPDATE_FREQ: "10.0",
            HYPOTHESIS_FAKER_DURATION: "0.1",
            HYPOTHESIS_FAKER_MAX_ITEMS: "100",
        }
        if env is not None:
            base.update(env)
        with TemporaryEnvironment(base):
            yield
