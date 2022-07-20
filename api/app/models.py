from codecs import unicode_escape_decode
from .database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String(255), unique=True, index=True)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    is_premium = Column(Boolean, default=False)

    urls = relationship('UrlTable')


class UrlTable(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    url = Column(String(255), index=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    shortened_url = Column(String(255), unique=True, index=True)
    clicks = Column(Integer, default=0)
    
    user = relationship('Users')
    
    



