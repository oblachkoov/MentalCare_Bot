from datetime import datetime
from sqlalchemy import Column, BigInteger, String, DateTime, ForeignKey
from models.base import Base


class Log(Base):
    __tablename__ = "logs"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.id'))
    action = Column(String)
    detail = Column(String)
    created_at = Column(DateTime, default=datetime.now)

