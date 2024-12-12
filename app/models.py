from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True, index=True)
    registration_number = Column(String, unique=True, index=True, nullable=False)
    model = Column(String, nullable=False)
    owner = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)


