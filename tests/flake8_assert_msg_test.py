import ast
from typing import Set

from flake8_assert_msg import Plugin


def results(s: str) -> Set[str]:
    return {"{}:{}: {}".format(*r) for r in Plugin(ast.parse(s)).run()}


def test_trivial() -> None:
    assert not results(""), "trivial input should be ok"


def test_normal_assignment_ok() -> None:
    assert not results('assert True, "foo"'), "assertion with msg should be ok"


def test_assignment_expression_not_ok() -> None:
    (msg,) = results("assert True")
    assert (
        msg == "1:0: ASS001 do not use bare asserts"
    ), "bare assert should raise a warning"
