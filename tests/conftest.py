"""Fixtures available to all tests in the package."""
import pytest
from geneweaver.testing.fixtures import *  # noqa: F403


@pytest.fixture(scope="session")
def package_submodule_name() -> str:
    """Return the name of the package submodule being tested."""
    return "framework"
