"""Root schemas for tool input and output."""
from pydantic import BaseModel


class ToolInput(BaseModel):
    """Base class for tool input schema."""


class ToolOutput(BaseModel):
    """Base class for tool output schema."""
