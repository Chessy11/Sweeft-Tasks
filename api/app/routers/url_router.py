from re import U
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from .. database import get_db
from .. import models
from .. import schemas, oauth2
from .. shorten import check_url
from .. import util
from fastapi.responses import RedirectResponse

router = APIRouter(  
    prefix="/urls",
    tags=["urls"] )
              
              



@router.post("/shorten/")
def create_link(url_to_shorten: schemas.URL, current_user: int = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    
 
    if not check_url(url_to_shorten.url):
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")

    url_relationship = util.find_with_basic(db, url=url_to_shorten.url, current_user=current_user.id)
    
    if url_relationship:
        context = {
            "url": url_relationship.url,
            "copy the following URL": "localhost:8000/urls/go/" + url_relationship.shortened_url,
            "user": current_user.username,
            "created": url_relationship.created_at,
        }
        return context
    
    
    return util.shorten_link(db, url=url_to_shorten.url, current_user=current_user.id)


    

@router.get("/go/{shortened_url}")
def get_link(shortened_url: str, db: Session = Depends(get_db)):
    relationship = util.find_shortened_url(db, shortened_url=shortened_url)
    if not relationship and shortened_url != 'docs':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
    util.update_clicks(db, url=relationship)
    destination = relationship.url
    return RedirectResponse(destination)




@router.get("/get-short/{id}")
def get_pair(id: int, current_user: int = Depends(oauth2.get_current_user),  db: Session = Depends(get_db)):
    user_data =  db.query(models.UrlTable).filter(models.UrlTable.user_id == id).all()

    if current_user.id != user_data[0].user_id:
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only view your own URLs")

    if not user_data:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No URLs found")
    
    return user_data



@router.post("/create-custom/")
def create_custom(custom_url: schemas.Shortener, current_user: int = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    if not check_url(custom_url.url):
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
    
    short_url = util.find_shortened_url(db, shortened_url=custom_url.shortened_url)
    if current_user.is_premium == False:
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You must be a premium user to create custom URLs")
    
    if short_url:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL already exists")
    if current_user.is_premium == True:
         util.create_link(db, url=custom_url.url, shortUrl=custom_url.shortened_url, current_user=current_user.id)
         context = {
            "url": custom_url.url,
            "copy following url": "localhost:8000/urls/go/" + custom_url.shortened_url
            
         }
         return context
         
