from enum import Enum


class IncidentType(Enum):
    SQL_FAILURE = "SQL_FAILURE"
    SCHEMA_MISMATCH = "SCHEMA_MISMATCH"
    DUPLICATE_RECORDS = "DUPLICATE_RECORDS"
    MISSING_DATA = "MISSING_DATA"
    PIPELINE_DELAY = "PIPELINE_DELAY"
    UNKNOWN = "UNKNOWN"


class Severity(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


INCIDENT_CATALOG = {
    IncidentType.SQL_FAILURE: {
        "description": "SQL query execution failure",
        "investigation_required": "Analyze SQL error and query dependencies",
    },
    IncidentType.SCHEMA_MISMATCH: {
        "description": "Unexpected change in source schema",
        "investigation_required": "Compare expected and actual schemas",
    },
    IncidentType.DUPLICATE_RECORDS: {
        "description": "Duplicate records detected",
        "investigation_required": "Identify duplicate keys and affected records",
    },
    IncidentType.MISSING_DATA: {
        "description": "Expected records are missing",
        "investigation_required": "Investigate source and destination record counts",
    },
    IncidentType.PIPELINE_DELAY: {
        "description": "Pipeline execution exceeded expected duration",
        "investigation_required": "Investigate task execution times and dependencies",
    },
    IncidentType.UNKNOWN: {
        "description": "Unrecognized pipeline incident",
        "investigation_required": "Investigate available execution metadata and logs",
    },
}