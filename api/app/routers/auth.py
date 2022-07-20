from fastapi import (
    Depends,
    APIRouter,
    HTTPException,
    status,
)
from fastapi.security import OAuth2PasswordRequestForm
from .. import models, schemas, auth_utils, database, oauth2
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/users",
    tags=["users"],
)



@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    
    hashed_password = auth_utils.get_password_hash(user.password)
    user.password= hashed_password
    new_user = models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user




@router.post("/login/", status_code=status.HTTP_200_OK, response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    
    user = db.query(models.Users).filter(models.Users.username == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    
    if not auth_utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}




@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, current_user: models.Users = Depends(oauth2.get_current_user), db: Session = Depends(database.get_db)):
    
    if current_user.id != id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user