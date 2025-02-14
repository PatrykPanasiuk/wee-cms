from fastapi import FastAPI
from backend.routes import router
from backend.database import Base, engine

# Tworzenie bazy danych (jeśli nie istnieje)
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Wee-CMS API is running!"}