
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
#DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL="postgresql+psycopg2://postgres:123@localhost:5432/testdb"
os.environ["PGCLIENTENCODING"] = "utf-8"

engine = create_engine(
    DATABASE_URL,
    echo=True  
)
print(repr(DATABASE_URL))
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()