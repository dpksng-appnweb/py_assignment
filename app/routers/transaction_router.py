from service.transaction_service import TransactionService
from fastapi import APIRouter, Depends
from dto.transaction_dto import TransactionDto
from typing import Optional
from sqlalchemy.orm import Session
from config import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def add(transaction: TransactionDto, db: Session = Depends(get_db)):
    transactionService = TransactionService()
    return transactionService.add(db, transaction)

@router.get("/")
async def getAll(customerId : Optional[str] = None, minAmount : float = 500 ,offset : int = 0, limit : int = 20, db: Session = Depends(get_db)):
    transactionService = TransactionService()
    return transactionService.getAll(db, customerId, minAmount, offset, limit)