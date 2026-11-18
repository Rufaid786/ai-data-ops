from enum import Enum

class IncidentType(Enum):
    # DATA_QUALITY = "Data Quality"
    SQL_FAILURE = "SQL_Failure"
    SCHEMA_MISMATCH = "SCHEMA_MISMATCH"
    DUPLICATE_RECORDS = "DUPLICATE_RECORDS"
    MISSING_DATA = "MISSING_DATA"
    PIPELINE_DELAY = "PIPELINE_DELAY"

class Severity(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"   


INCIDENT_CATALOG = {
    IncidentType.SQL_FAILURE: {
        "description": "SQL query execution failure",  
        "investigation_required": "Analyze SQL error and query dependencies"
    },
    IncidentType.SCHEMA_MISMATCH: {
        "description": "Unexpected change in source schema",
        "investigation_required": "Compare expected and actual schemas"
    },
    IncidentType.DUPLICATE_RECORDS: {
        "description": "Duplicate records detected",
        "investigation_required": "Identify duplicate keys and affected records"
    },
    IncidentType.MISSING_DATA: {
        "description": "Expected records are missing",       
        "investigation_required": "Investigate source and destination record counts"
    },
    IncidentType.PIPELINE_DELAY: {
        "description": "Pipeline execution exceeded expected duration",                        
        "investigation_required": "Investigate task execution times and dependencies"
    }
}

