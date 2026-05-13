from sqlalchemy import Column, Integer, String, ForeignKey
from unittest.mock import Base

class Chat(Base):
    __tablename__ = "chats"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))
    message = Column(String)
    response = Column(String)
    timestamp = Column(String)
    intent = Column(String)
