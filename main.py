from fastapi import FastAPI
from routers.router import router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(router)
 
origins = [
    "http://localhost:3000",
]

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


