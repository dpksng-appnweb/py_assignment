from pydantic import BaseModel

class TransactionDto(BaseModel):
    customerId: str
    receivedDateTime: str
    amount: float
    cardNumber: str
    cardExpiry: str
    cvv: str
    city: str
    referenceId: str