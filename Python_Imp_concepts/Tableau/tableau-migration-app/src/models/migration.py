from pydantic import BaseModel, Field

class MigrationInput(BaseModel):
    dashboard_name: str = Field(..., title="Dashboard Name", max_length=255)
    source_path: str = Field(..., title="Source Path", regex=r"^.+\..+$")
    destination_path: str = Field(..., title="Destination Path", regex=r"^.+\..+$")