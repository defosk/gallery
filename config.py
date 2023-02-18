from pydantic import BaseSettings


class Settings(BaseSettings):
    IMAGE_DIR: str = '.'
    items_per_user: int = 50
