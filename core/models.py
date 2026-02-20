from sqlalchemy import Column, Integer, Text, DateTime, Boolean, String, JSON, ForeignKey
from core.database import Base
from datetime import datetime

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    role = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.now)
    is_cache = Column(Boolean, default=True)
    session_id = Column(String(36), nullable=True)


class LongMemory(Base):
    __tablename__ = "long_memory"
    
    id = Column(Integer, primary_key=True)
    user_message_id = Column(Integer, ForeignKey('messages.id'))
    assistant_message_id = Column(Integer, ForeignKey('messages.id'))
    session_id = Column(String(36), nullable=False)
    saved_at = Column(DateTime, default=datetime.now)
    summary = Column(Text, nullable=True)
    meta_data = Column(JSON, nullable=True) 