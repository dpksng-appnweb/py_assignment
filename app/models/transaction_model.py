from sqlalchemy import Boolean, Column, String, Float
from config import Base, engine

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(String, primary_key = True)
    created = Column(String)
    updated = Column(String)
    active = Column(Boolean, default = True)
    customerId = Column(String)
    receivedDateTime = Column(String)
    amount = Column(Float)
    city = Column(String)
    referenceId = Column(String)
    mode = Column(String, default = "CREDIT_CARD")