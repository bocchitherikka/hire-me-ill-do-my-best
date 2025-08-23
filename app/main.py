from fastapi import FastAPI
from . import database, models, routers

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(routers.router)