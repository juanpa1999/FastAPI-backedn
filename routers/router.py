from fastapi import APIRouter
from routers import auth, hero

router= APIRouter()
router.include_router(auth.router)
router.include_router(hero.router)