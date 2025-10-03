from pydantic_settings import BaseSettings
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    DB_ROUTE: str

    debug: bool = True

    TEMPLATES_DIR: Path = BASE_DIR / 'app' / 'templates'
    STATIC_URL: str = '/static'
    STATIC_DIR: Path = BASE_DIR / 'app' / 'static'

    def mount_static(self, app):
        if self.STATIC_DIR.exists():
            app.mount(
                self.STATIC_URL,
                StaticFiles(directory=self.STATIC_DIR),
                name='static'
            )
        else:
            raise RuntimeError(f'Static directory not found: {self.STATIC_DIR}')

    def configure_templates(self):
        templates = Jinja2Templates(directory=self.TEMPLATES_DIR)
        templates.env.globals['url_for'] = lambda name, **params: f'/static/{params.get("filename", "")}'
        return templates

    @property
    def database_url(self) -> str:
        return f'{self.DB_ROUTE}'

    class Config:
        env_file = '.env'


settings = Settings()