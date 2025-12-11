from pydantic import BaseModel, validator
from typing import Any, Dict

class MigrationInput(BaseModel):
    dashboard_name: str
    source_path: str
    destination_path: str

    @validator('dashboard_name')
    def validate_dashboard_name(cls, v):
        if not v:
            raise ValueError('Dashboard name cannot be empty')
        return v

    @validator('source_path', 'destination_path')
    def validate_path(cls, v):
        if not v.startswith('/'):
            raise ValueError('Path must start with a "/"')
        return v

def simulate_migration(migration_input: MigrationInput) -> Dict[str, Any]:
    # Simulate the migration process
    response = {
        "status": "success",
        "message": f"Migration of dashboard '{migration_input.dashboard_name}' from '{migration_input.source_path}' to '{migration_input.destination_path}' simulated successfully."
    }
    return response