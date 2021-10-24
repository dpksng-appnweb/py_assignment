from dto.transaction_dto import TransactionDto
from crud import transaction_crud as transactionCrud
from sqlalchemy.orm import Session
from models.transaction_model import Transaction as TransactionModel

class TransactionService:

    def add(self, db: Session, transaction: TransactionDto):
        entity = TransactionModel()
        entity.customerId = transaction.customerId
        entity.receivedDateTime = transaction.receivedDateTime
        entity.amount = transaction.amount
        entity.city = transaction.city
        entity.referenceId = transaction.referenceId
        entity.mode = "CREDIT_CARD"
        return transactionCrud.create(db, entity)

    def getAll(self, db: Session, customerId : str, minAmount : float, offset : int, limit : int):
        return transactionCrud.getAll(db, offset, limit)