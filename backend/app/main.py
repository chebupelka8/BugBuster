from typing import Literal

from fastapi import FastAPI
import uvicorn

from api.v1 import router as api_router_v1

from contextlib import asynccontextmanager

from core.database import AbstractDataBase


@asynccontextmanager
async def lifespan(_: FastAPI):
    await AbstractDataBase.create_all_tables()
    yield


app = FastAPI(
    title="BugBuster",
    lifespan=lifespan
)

app.include_router(api_router_v1)


@app.get("/home")
async def home() -> dict[Literal["home"], Literal["welcome"]]:
    await AbstractDataBase.create_all_tables()

    return {
        "home": "welcome"
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)

