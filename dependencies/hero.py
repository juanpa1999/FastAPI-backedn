import jwt
from typing import Annotated
from fastapi import Query, Depends, HTTPException, Path
from models.user import User, UserId
from models.hero import Hero, HeroCreate, HeroUpdate
from internal.db import SessionDep, select
from dependencies.auth import oauth2_scheme, SECRET_KEY, ALGORITHM


def create_hero(
        hero: HeroCreate, 
        session: SessionDep, 
        token: Annotated[str, Depends(oauth2_scheme)]
):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    user_id = int(payload.get("sub"))
    db_hero = Hero(**hero.dict(), user_id=user_id)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


async def read_heros(
        session: SessionDep, 
        token: Annotated[str, Depends(oauth2_scheme)], 
        offset: int | None = 0,
        limit: Annotated[int | None, Query(le=100)] = 100,
):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    user_id = int(payload.get("sub"))
    heroes = await session.exec(select(Hero).where(Hero.user_id == user_id).offset(offset).limit(limit))
    return heroes.scalars().all()


def read_hero(
        hero_id: Annotated[int, Path()], 
        session: SessionDep,
        token: Annotated[str, Depends(oauth2_scheme)]
):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    user_id = int(payload.get("sub"))
    hero = session.exec(
        select(Hero).where((Hero.id == hero_id) & (Hero.user_id == user_id))
    ).first()
    if hero is None:
        raise HTTPException (status_code=404, detail="Hero not found")
    return hero
    

def update_hero(
        hero_id: Annotated[int, Path()], 
        hero: HeroUpdate,
        session: SessionDep,
        token: Annotated[str, Depends(oauth2_scheme)]
):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    user_id = int(payload.get("sub"))
    hero_db = session.exec(
        select(Hero).where((Hero.id == hero_id) & (Hero.user_id == user_id))
    ).first()
    if hero_db is None:
        raise HTTPException (status_code=404, detail="Hero not found")
    hero_data = hero.model_dump(exclude_unset=True)
    hero_db.sqlmodel_update(hero_data)
    session.add(hero_db)
    session.commit()
    session.refresh(hero_db)
    return hero_db


def delete_hero(
        hero_id: Annotated[int, Path()], 
        session: SessionDep,
        token: Annotated[str, Depends(oauth2_scheme)]
):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    user_id = int(payload.get("sub"))
    hero = session.exec(
        select(Hero).where((Hero.id == hero_id) & (Hero.user_id == user_id))
    ).first()
    if hero is None:
        raise HTTPException (status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {f"Hero {hero.name}": "deleted"}