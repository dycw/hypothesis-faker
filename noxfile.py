from multiprocessing import cpu_count

from nox import Session
from nox import options
from nox import session


options.reuse_existing_virtualenvs = True
options.error_on_missing_interpreters = True
options.error_on_external_run = True


@session(python=["3.7", "3.8", "3.9", "3.10"])
def test(session: Session) -> None:
    session.install("-r", "requirements-all.txt")
    n = max(round(cpu_count() / 2), 1)
    _ = session.run("pytest", f"-n={n}")
