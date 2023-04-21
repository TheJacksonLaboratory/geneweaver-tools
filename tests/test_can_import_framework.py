"""Test that we can import geneweaver.tools.framework."""
import importlib

import pytest

submodule_to_import = ["framework"]


@pytest.mark.parametrize("submodule", submodule_to_import)
def test_can_import_absolute(submodule: str) -> None:
    """Test that we can import tool submodules with absolute import."""
    module = importlib.import_module(f"geneweaver.tools.{submodule}")
    assert module is not None


@pytest.mark.parametrize("submodule", submodule_to_import)
def test_can_import_relative(submodule: str) -> None:
    """Test that we can import tool submodules with relative import."""
    module = importlib.import_module(f".tools.{submodule}", "geneweaver")
    assert module is not None


@pytest.mark.parametrize("submodule", submodule_to_import)
def test_submodule_available_from_namespace_package(submodule: str) -> None:
    """Test that we can import tool submodules from the geneweaver namespace package."""
    from geneweaver import tools

    assert hasattr(tools, submodule)
    assert getattr(tools, submodule) is not None
