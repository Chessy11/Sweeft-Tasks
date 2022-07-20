from token import OP
from venv import create
from pydantic import BaseModel, AnyUrl
from typing import Optional
from uuid import uuid4
from datetime import datetime



class UserCreate(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    created_at: datetime
    
    class Config:
        orm_mode = True
        
        
class UserLogin(BaseModel):
    username: str
    password: str
    

class Token(BaseModel):
    access_token: str
    token_type: str



class TokenData(BaseModel):
    id: Optional[int] = None



class URL(BaseModel):
    url: AnyUrl
    
    
    
class Shortener(BaseModel):
    url: str
    shortened_url: str
    
class Shortened(URL):
    clicks: int
    
    class Config:
        orm_mode = True
        
        