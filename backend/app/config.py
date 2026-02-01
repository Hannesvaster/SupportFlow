from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    jwt_secret: str = "CHANGE_ME_IN_PROD"
    jwt_algorithm: str = "HS256"
    access_token_exp_minutes: int = 60

settings = Settings()
