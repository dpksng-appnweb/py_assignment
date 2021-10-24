from service.customer_service import CustomerService
from fastapi import APIRouter, Depends
from dto.customer_dto import CustomerDto
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
async def add(customer: CustomerDto, db: Session = Depends(get_db)):
    customerService = CustomerService()
    return customerService.add(db, customer)

@router.get("/")
async def getAll(year : Optional[int] = None, offset : int = 0, limit : int = 20, db: Session = Depends(get_db)):
    customerService = CustomerService()
    return customerService.getAll(db, year, offset, limit)
