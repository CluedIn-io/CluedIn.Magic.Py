# pylint: disable=missing-module-docstring missing-function-docstring
import pytest

from ..ctx import get_ipython_shell


@pytest.fixture(name="ipython_shell", scope="module")
def fixture_ipython_shell():
    return get_ipython_shell()


def test_get_context_failure(ipython_shell, capsys):
    # Arrange
    line = 'get-context --jwt invalid_token'

    # Act
    context = ipython_shell.run_line_magic('cluedin', line)

    # Assert
    assert context is None
    assert \
        'not enough values to unpack (expected 3, got 1)\n' == \
        capsys.readouterr().out
