from fastapi import APIRouter, Depends
from typing import Annotated
from models.hero import HeroPublic, Hero
from dependencies.auth import get_current_active_user
from dependencies.hero import read_heros, create_hero, read_hero, delete_hero, update_hero


router = APIRouter(
    prefix="/heroes",
    tags=["Heroes, create, update, delete by User verification"],
    dependencies=[Depends(get_current_active_user)]
)


@router.post("/", response_model=HeroPublic)
def create_hero(hero: Annotated[Hero, Depends(create_hero)]):
    return hero


@router.get("/", response_model=list[HeroPublic])
def read_heroes(heroes: Annotated[list[HeroPublic], Depends(read_heros)]):
    return heroes
    

@router.get("/{hero_id}", response_model=HeroPublic)
def read_hero(hero: Annotated[Hero, Depends(read_hero)]):
    return hero


@router.put("/{hero_id}", response_model=HeroPublic)
def update_hero(hero_db: Annotated[Hero, Depends(update_hero)]):
    return hero_db


@router.delete("/{hero_id}")
def delete_hero(hero: Annotated[Hero, Depends(delete_hero)]):
    return hero