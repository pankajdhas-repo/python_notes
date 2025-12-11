from fastapi import FastAPI
from api.endpoints import router as migration_router

app = FastAPI()

app.include_router(migration_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tableau Migration API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)