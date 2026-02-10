from core.models import Message
from core.database import Session

session = Session()

def save_message(
    role: str,
    content: str, 
    is_cache: bool = True,
    session_id: str = None
):
    msg = Message(
        role=role, 
        content=content,
        is_cache=is_cache,
        session_id=session_id
    )
    session.add(msg)
    session.commit()


def get_cache_messages(limit: int = 20) -> list:
    messages = (
        session.query(Message)
        .filter(Message.is_cache == True)
        .order_by(Message.timestamp.desc())  
        .limit(limit)
        .all()
    )
    messages.reverse()
    
    history = []
    for msg in messages:
        history.append({
            "role": msg.role,
            "content": msg.content
        })
    
    return history


def clear_cache():
    session.query(Message).filter(Message.is_cache == True).delete()
    session.commit()


def load_history(limit=10):
    return (
        session.query(Message)
        .order_by(Message.timestamp)
        .limit(limit)
        .all()
    )