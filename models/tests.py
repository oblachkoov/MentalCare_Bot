from sqlalchemy import Column, BigInteger, String
from models.base import Base


class Test(Base):
    __tablename__ = "tests"
    id = Column(BigInteger, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)


