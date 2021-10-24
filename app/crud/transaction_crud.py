from sqlalchemy.orm import Session
from models.transaction_model import Transaction
import uuid
import datetime

def create(db: Session, entity: Transaction): 
    entity.id = uuid.uuid1()
    entity.created = datetime.datetime.now()
    entity.updated = datetime.datetime.now()
    entity.active = True
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity

def getAll(db: Session, offset: int = 0, limit: int = 100):
    return db.query(Transaction).offset(offset).limit(limit).all()