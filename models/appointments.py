from datetime import datetime
from sqlalchemy import Column, BigInteger, String, DateTime, ForeignKey
from models.base import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(BigInteger, primary_key=True)

    client_id = Column(
        BigInteger,
        ForeignKey("users.id"),
        nullable=False
    )

    psychologist_id = Column(
        BigInteger,
        ForeignKey("psychologists.id"),
        nullable=False
    )

    time = Column(DateTime)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
