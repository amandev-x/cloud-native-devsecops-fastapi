from fastapi import FastAPI 
from api import router

app = FastAPI(
    title="Cloud Native DevSecops FastAPI"
)

app.include_router(router)
