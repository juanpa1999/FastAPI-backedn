from datetime import timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, status, Body, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from models.token import Token
from models.user import UserBase, User, UserId, UserRegister
from internal.db import *
from dependencies.auth import get_current_active_user, get_password_hash, authenticate_user, create_access_token

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(
    tags=["User registration & verification"]
)


@router.post("/register", response_model=UserBase)
async def register_user(
    user: Annotated[UserRegister, Body()], session: SessionDep
):
    existing_user = session.exec(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
        )
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User or email already in system."
        )
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        password=hashed_password,  
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: SessionDep
) -> Token:
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id), "username": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/users/me/", response_model=UserId)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[UserId, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username, "id": current_user.id}]