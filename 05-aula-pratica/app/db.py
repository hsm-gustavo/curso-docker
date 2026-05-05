import os
from typing import Generator
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise EnvironmentError("DATABASE_URL não foi configurada")

engine = create_engine(DATABASE_URL, echo=True)


def get_session() -> Generator[Session]:
    with Session(engine) as session:
        yield session


def create_tables() -> None:
    from app.models import Base

    Base.metadata.create_all(bind=engine)
