import enum


class WorkflowType(enum.Enum):
    """Type of workflow"""
    WDL = 'WDL'
    Nextflow = 'Nextflow'
