from core.models import Message
from core.database import Session

session = Session()

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