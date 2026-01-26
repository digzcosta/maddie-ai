from sqlalchemy import Column, Integer, Text, DateTime
from core.database import Base
from datetime import datetime

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    role = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.now())