"""Abstract classes for tools."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional, Type

from .enum import WorkflowType
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
        return Path(__file__).parent / "static"

    @property
    def workflow_definition(self: AbstractTool) -> Optional[Path]:
        """Location of workflow definition for the tool."""
        workflow_path = Path(__file__).parent / "workflow.nf"
        return workflow_path if workflow_path.is_file() else None

    @property
    def workflow_type(self: AbstractTool) -> Optional[WorkflowType]:
        """The type of workflow used by workflow definition."""
        return WorkflowType.NEXTFLOW
