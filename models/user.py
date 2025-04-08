from sqlmodel import Field, SQLModel
from pydantic import EmailStr


class UserBase(SQLModel):
    username: str = Field(index=True)
    email: EmailStr | None = None
    full_name: str | None = None
    disabled: bool | None = False


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str

class UserId(UserBase):
    id: int | None = Field(default=None, primary_key=True)

class UserRegister(UserBase):
    password: str
