from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine, select


postgres_url = "postgresql://admin:admin123@localhost:5432/pablo_db"
engine = create_engine(postgres_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session



SessionDep = Annotated[Session, Depends(get_session)]