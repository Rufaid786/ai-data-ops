
import json
import re

from datetime import datetime

from ai_dataops.incident import Incident
from ai_dataops.incident_catalog import IncidentType, Severity


def classify_incident(logs: str) -> tuple[IncidentType, Severity]:
    logs = logs.lower()

    if "duplicate transaction_id detected" in logs:
        return IncidentType.DUPLICATE_RECORDS, Severity.HIGH

    elif "invalid identifier" in logs or "sql compilation error" in logs:
        return IncidentType.SQL_FAILURE, Severity.HIGH

    elif "schema mismatch" in logs or "unexpected column" in logs:
        return IncidentType.SCHEMA_MISMATCH, Severity.HIGH

    elif "missing records" in logs or "record count mismatch" in logs:
        return IncidentType.MISSING_DATA, Severity.MEDIUM

    elif "connection timeout" in logs or "pipeline exceeded expected duration" in logs:
        return IncidentType.PIPELINE_DELAY, Severity.HIGH

    else:
        return IncidentType.UNKNOWN, Severity.MEDIUM


def extract_duplicate_count(incident_type: IncidentType, logs: str) -> int | None:

    if incident_type == IncidentType.DUPLICATE_RECORDS:
        match = re.search(r"Found (\d+) duplicate records", logs)

        if match:
            return int(match.group(1))

    return None


def normalize_incident(metadata_path: str, log_path: str) -> Incident:

    # Step 1: Read Airflow metadata
    with open(metadata_path, "r") as file:
        metadata = json.load(file)

    # Step 2: Validate task state
    if metadata["state"] != "failed":
        raise ValueError("Airflow task is not in failed state")

    # Step 3: Read application logs
    with open(log_path, "r") as file:
        logs = file.read()

    # Step 4: Classify incident
    incident_type, severity = classify_incident(logs)

    # Step 5: Extract error message
    error_message = logs.strip()

    # Step 6: Extract duplicate count
    duplicate_count = extract_duplicate_count(incident_type, logs)

    if incident_type == IncidentType.DUPLICATE_RECORDS and duplicate_count is None:
        raise ValueError("Duplicate count not found in logs")

    # Step 7: Create standardized Incident
    incident = Incident(
        incident_id=metadata["run_id"],
        pipeline_name=metadata["dag_id"],
        task_name=metadata["task_id"],
        incident_type=incident_type,
        severity=severity,
        timestamp=datetime.fromisoformat(metadata["timestamp"]),
        error_message=error_message,
        source="AIRFLOW",
        actual=duplicate_count
    )

    return incident
