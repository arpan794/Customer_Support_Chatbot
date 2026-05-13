from sqlalchemy import Column, Integer, String, ForeignKey
from unittest.mock import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    company_id = Column(Integer, ForeignKey("companies.id"))