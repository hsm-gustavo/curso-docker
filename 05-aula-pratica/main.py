from fastapi import FastAPI

from app import db
from app.routes import router as tasks_router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.create_tables()
    yield


def create_app() -> FastAPI:
    app = FastAPI(title="TODO Curso", lifespan=lifespan)

    app.include_router(tasks_router)

    return app


app = create_app()
