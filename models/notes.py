from datetime import datetime
from sqlalchemy import Column, BigInteger, String, DateTime, ForeignKey
from models.base import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    text = Column(String)
    file_url = Column(String)
    created_at = Column(DateTime, default=datetime.now)


