from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, constr
from services.migration_service import simulate_migration

router = APIRouter()

class MigrationInput(BaseModel):
    dashboard_name: constr(min_length=1) # type: ignore
    source_path: constr(min_length=1) # type: ignore
    destination_path: constr(min_length=1) # type: ignore

@router.post("/migrate")
async def migrate_dashboard(migration_input: MigrationInput):
    try:
        result = simulate_migration(migration_input)
        return {"status": "success", "message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))