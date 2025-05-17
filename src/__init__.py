'''Fast API Application'''

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware





@asynccontextmanager
async def lifespan(app: FastAPI):
    """"
    Async context manager for app lifespan.This function initializes the database"
    """

    try:
        yield
    finally:

        pass


def create_app():
    '''Initialization Fast API App'''
    app = FastAPI(title="Data Science",lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    from src.routes.router import pilot
    app.include_router(pilot)


    return app
