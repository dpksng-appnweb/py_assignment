from sqlalchemy.orm import Session
from models.customer_model import Customer
import uuid
import datetime

def create(db: Session, entity: Customer):
    entity.id = uuid.uuid1()
    entity.created = datetime.datetime.now()
    entity.updated = datetime.datetime.now()
    entity.active = True
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity

def getAll(db: Session, offset: int = 0, limit: int = 100):
    return db.query(Customer).offset(offset).limit(limit).all()

