from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import settings



SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.pg_user}:{settings.pg_pwd}@{settings.pg_host}:{settings.pg_port}/{settings.pg_name}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
        
def get_user(user_id: int):
    db = SessionLocal()
    user = db.query(models.User).get(user_id)
    db.close()
    return user