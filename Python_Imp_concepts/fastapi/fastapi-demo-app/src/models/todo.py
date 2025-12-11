from pydantic import BaseModel

class ToDo(BaseModel):
    id: int
    name: str
    description: str