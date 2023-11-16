"""Test default properties/methods of the AbstractTool class."""
import sys
from pathlib import Path
from typing import Type

import pytest
from geneweaver.tools.framework.abstract import AbstractTool, ToolInput, ToolOutput


def _create_tool_subclass(name: str) -> type:
    return type(
        name,
        (AbstractTool,),
        {
            "tool_input": property(lambda self: Type[ToolInput]),
            "tool_output": property(lambda self: Type[ToolOutput]),
            "run": lambda self, tool_input: ToolOutput(),
        },
    )


@pytest.mark.parametrize("tool_name", ["ToolA", "ToolB", "ToolC"])
def test_tool_name(tool_name: str) -> None:
    """Test that the tool gets its name from the class name by default."""
    tool_class = _create_tool_subclass(tool_name)
    tool_instance = tool_class()
    assert tool_instance.tool_name == tool_name


@pytest.mark.parametrize("tool_name", ["ToolA", "ToolB", "ToolC"])
def test_static_files_location(tool_name: str) -> None:
    """Test that the tool has expected default static files location."""
    tool_class = _create_tool_subclass(tool_name)
    tool_instance = tool_class()
    expected_path = (
        Path(sys.modules[tool_instance.__module__].__file__).parent / "static"
    )

    assert tool_instance.static_files_location.resolve() == expected_path.resolve()
