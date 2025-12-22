from datetime import datetime

from sqlalchemy import Column, BigInteger, String, DateTime, ForeignKey
from models.base import Base


class Result(Base):
    __tablename__ = "results"

    id = Column(BigInteger, primary_key=True)

    test_id = Column(
        BigInteger,
        ForeignKey("tests.id"),
        nullable=False
    )

    user_id = Column(
        BigInteger,
        ForeignKey("users.id"),
        nullable=False
    )

    total_score = Column(BigInteger)
    interpretation = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
