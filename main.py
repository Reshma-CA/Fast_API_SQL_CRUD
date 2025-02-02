from fastapi import FastAPI
from routes import router
import models
from database import engine

# Create tables in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes
app.include_router(router)

