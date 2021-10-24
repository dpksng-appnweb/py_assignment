from dto.customer_dto import CustomerDto
from crud import customer_crud as customerCrud
from sqlalchemy.orm import Session
from models.customer_model import Customer as CustomerModel

class CustomerService:

    def add(self, db: Session, customer: CustomerDto):
        entity = CustomerModel()
        entity.name = customer.name
        entity.email = customer.email
        return customerCrud.create(db, entity)

    def getAll(self, db: Session, year : int, offset : int, limit : int):
        return customerCrud.getAll(db, offset, limit)