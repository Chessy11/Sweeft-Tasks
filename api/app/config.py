from this import s
from pydantic import BaseSettings

class Settings(BaseSettings):
    pg_name: str
    pg_user: str
    pg_port: int
    pg_pwd : str
    pg_host: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    
    class Config:
        env_file = '.env'
        
        
settings = Settings()