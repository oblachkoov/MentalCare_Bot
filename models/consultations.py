from datetime import datetime
from sqlalchemy import Column, BigInteger, String, DateTime, ForeignKey
from models.base import Base


class Consultation(Base):
    __tablename__ = "consultations"

    id = Column(BigInteger, primary_key=True)

    appointment_id = Column(
        BigInteger,
        ForeignKey("appointments.id"),
        nullable=False
    )

    psychologist_id = Column(
        BigInteger,
        ForeignKey("psychologists.id"),
        nullable=False
    )

    notes = Column(String)
    file_url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
