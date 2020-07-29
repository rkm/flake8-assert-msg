import subprocess

import pytest


def test_valid(tmpdir) -> None:  # type: ignore
    path = tmpdir / "good.py"
    with open(path, "w") as f:
        f.write("assert True, 'ok'\n")
    subprocess.check_call(("flake8", path))


def test_invalid(tmpdir) -> None:  # type: ignore
    path = tmpdir / "bad.py"
    with open(path, "w") as f:
        f.write("assert True\n")
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_call(("flake8", path))
