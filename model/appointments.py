from sqlalchemy import Column, BigInteger, ForeignKey, DateTime, String, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from model.base import Base  # твой Base

import enum


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    client_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    psychologist_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    time = Column(DateTime, nullable=True)
    status = Column(String(20),default="new", nullable=False)
    created_at = Column(DateTime, default=datetime.now)


