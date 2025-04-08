
from sqlmodel import Field, SQLModel
from pydantic import BaseModel, EmailStr


class HeroBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)


class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    secret_name: str
    user_id: int = Field(foreign_key="user.id")


class HeroPublic(HeroBase):
    id: int


class HeroCreate(HeroBase):
    secret_name: str

class HeroUpdate(HeroBase):
    name: str | None = None
    age: int | None = None
    secret_name: str | None = None


