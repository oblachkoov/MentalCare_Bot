from sqlalchemy import Column, BigInteger, String, ForeignKey
from models.base import Base


class Answer(Base):
    __tablename__ = "answers"

    id = Column(BigInteger, primary_key=True)
    question_id = Column(BigInteger, ForeignKey('questions.id'))
    option_text = Column(String, nullable=False)
    score = Column(BigInteger)

