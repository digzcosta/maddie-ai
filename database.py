from sqlalchemy import create_engine, Column, Integer, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

engine = create_engine("sqlite:///maddie.db")

Base = declarative_base()

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    role = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.now())

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


session = Session()

# Functions

def save_message(role, content):
    msg = Message(role=role, content=content)
    session.add(msg)
    session.commit()

def load_history(limit=10):
    return (
        session.query(Message)
        .order_by(Message.timestamp)
        .limit(limit)
        .all()
    )

