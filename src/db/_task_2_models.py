from sqlalchemy import CheckConstraint, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ShortNames(Base):
    __tablename__ = "short_names"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    status = Column(Integer)

    __table_args__ = (CheckConstraint("status IN (0, 1)", name="check_status_range"),)


class FullNames(Base):
    __tablename__ = "full_names"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    status = Column(Integer)
