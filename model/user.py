from sqlalchemy import Column, BigInteger, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from model.base import Base

from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    full_name = Column(String)
    role = Column(String)

    notes = relationship("Note", back_populates="user", cascade="all, delete-orphan")


