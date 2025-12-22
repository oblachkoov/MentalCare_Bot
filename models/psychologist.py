from sqlalchemy import Column, BigInteger, String, ForeignKey, Boolean
from models.base import Base


class Psychologist(Base):
    __tablename__ = "psychologists"

    id = Column(BigInteger, primary_key=True)

    user_id = Column(
        BigInteger,
        ForeignKey("users.id"),
        nullable=False
    )

    full_name = Column(String)
    specialization = Column(String)
    experience = Column(String)
    certificate_url = Column(String)
    verified = Column(Boolean, default=False)
