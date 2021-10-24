from sqlalchemy import Boolean, Column, String
from config import Base

class Customer(Base):
    __tablename__ = "customers"
    id = Column(String, primary_key = True)
    created = Column(String)
    updated = Column(String)
    active = Column(Boolean, default = True)
    name = Column(String)
    email = Column(String, unique = True)