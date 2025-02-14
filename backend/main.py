from fastapi import FastAPI
from backend.routes import router
from backend.database import Base, engine

app = FastAPI()

# Create tables if not exists
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(router)