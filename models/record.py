from services.database_service import Base
from sqlalchemy import Column, DateTime, String, Integer


class Record(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    created_at = Column(type_=DateTime)
    topic = Column(type_=String)
    payload = Column(type_=String)
