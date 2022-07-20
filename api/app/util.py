from sqlalchemy.orm import Session
from . import models, schemas
from .shorten import shorten


def shorten_link(db: Session, url: schemas.URL, current_user: int):
    get_shortened_url = models.UrlTable(user_id=current_user, url=url, shortened_url=shorten(url))

    db.add(get_shortened_url)
    db.commit()
    db.refresh(get_shortened_url)
    return get_shortened_url



def find_shortened_url(db: Session, shortened_url: str):
    return db.query(models.UrlTable).filter(models.UrlTable.shortened_url == shortened_url).first()




def find_with_basic(db: Session, url: str, current_user: int):
    return db.query(models.UrlTable).filter(models.UrlTable.url == url, models.UrlTable.user_id == current_user).first()
        
def update_clicks(db: Session, url: schemas.Shortened):
    url.clicks += 1
    db.commit()
    db.refresh(url)
    return url
    
    
    
    
def create_link(db: Session, url: str, shortUrl: str, current_user: int):
    db_url = models.UrlTable(url=url, shortened_url=shortUrl, user_id=current_user)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url