from sqlalchemy import create_engine, Column, Integer, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

engine = create_engine("sqlite:///memory.db")

Base = declarative_base()

Session = sessionmaker(bind=engine)

