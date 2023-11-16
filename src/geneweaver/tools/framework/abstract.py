"""Abstract classes for tools."""

from __future__ import annotations

import sys
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Type

from .schema import ToolInput, ToolOutput


class AbstractTool(ABC):
    """Abstract class for GeneWeaver tools."""

    @abstractmethod
    def run(self: AbstractTool, tool_input: ToolInput) -> ToolOutput:
        """Run the tool."""

    @property
    @abstractmethod
    def tool_input(self: AbstractTool) -> Type[ToolInput]:
        """Input schema for the tool."""

    @property
    @abstractmethod
    def tool_output(self: AbstractTool) -> Type[ToolOutput]:
        """Output schema for the tool."""

    @property
    def tool_name(self: AbstractTool) -> str:
        """Return the name of the tool."""
        return self.__class__.__name__

    @property
    def static_files_location(self: AbstractTool) -> Path:
        """Location of static files for the tool."""
        module = sys.modules[self.__class__.__module__]
        module_path = Path(module.__file__).parent
        return module_path / "static"
