from fastapi import FastAPI

from app.routes.main import main_router
from app.config import settings


app = FastAPI()


settings.mount_static(app)
app.include_router(main_router)
