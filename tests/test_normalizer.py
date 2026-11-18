from pathlib import Path
from ai_dataops.normalizer import  normalize_incident


metadata_path = "data/incidents/airflow_metadata.json"

log_files = [
    "duplicate_records.log",
    "sql_failure.log",
    "schema_mismatch.log",
    "missing_data.log",
    "pipeline_delay.log",
    "unknown_error.log",
]

for log_file in log_files:

    log_path = str(Path("data/logs") / log_file)

    try:
        incident = normalize_incident(metadata_path, log_path)

        print(f"\nFile: {log_file}")
        print(f"Incident type: {incident.incident_type.value}")
        print(f"Severity: {incident.severity.value}")
        print(f"Actual: {incident.actual}")

    except Exception as error:
        print(f"\nFile: {log_file}")
        print(f"Error: {error}")

