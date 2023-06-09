from fastapi import FastAPI
import app.routes as routes
import app.config as config
from app.models.models import Base

app = FastAPI()

Base.metadata.create_all(bind=config.engine)  # обязательно в main 1 раз
app.include_router(routes.router)
