#
# uvicorn app.main:app --reload
from fastapi import FastAPI


from app.db.session import engine
from app.db.base import Base
import app.models.models

app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/ping")
def ping():
    return {"ping": "pong!"}

