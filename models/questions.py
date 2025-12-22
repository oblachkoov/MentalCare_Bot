from sqlalchemy import Column, BigInteger, String, ForeignKey
from models.base import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(BigInteger, primary_key=True)
    test_id = Column(BigInteger, ForeignKey('tests.id'))
    text = Column(String, nullable=False)