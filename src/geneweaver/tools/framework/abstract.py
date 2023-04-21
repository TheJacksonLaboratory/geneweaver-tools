from abc import ABC, abstractmethod
from pydantic import BaseModel
from pathlib import Path
from typing import Optional
from .enum import WorkflowType


class AbstractTool(ABC):

    @abstractmethod
    def run(self, *args, **kwargs) -> str:
        ...

    @abstractmethod
    def input(self) -> BaseModel:
        ...

    @abstractmethod
    def output(self) -> BaseModel:
        ...

    @property
    @abstractmethod
    def static_files_location(self) -> Path:
        ...

    @property
    @abstractmethod
    def workflow_definition(self) -> Optional[str]:
        ...

    @property
    @abstractmethod
    def workflow_type(self) -> Optional[WorkflowType]:
        ...
