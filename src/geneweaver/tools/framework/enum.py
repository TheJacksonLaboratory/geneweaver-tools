"""Enums for tool framework."""

import enum


class WorkflowType(enum.Enum):
    """Type of workflow."""

    WDL = "WDL"
    NEXTFLOW = "Nextflow"
