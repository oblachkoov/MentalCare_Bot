from sqlalchemy import Column, String, BigInteger, DateTime
from models.base import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    full_name = Column(String)
    phone = Column(String)
    role = Column(String, default="client")
    status = Column(String, default="active")
    registered_at = Column(DateTime, default=datetime.now)
    last_activity = Column(DateTime)
    language = Column(String, default="en")