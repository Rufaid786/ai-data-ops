from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .incident_catalog import IncidentType, Severity


#To represent all our errors in a common format
@dataclass
class Incident:
    incident_id: str
    pipeline_name: str
    task_name: str

    incident_type: IncidentType
    severity: Severity

    timestamp: datetime

    error_message: str

    source:str

    expected:Optional[str]=None
    actual: int | None = None

