from fastapi import FastAPI
from routers.customer_router import router as customerRouter
from routers.transaction_router import router as transactionRouter


BASE_URL = "/assignment/api/v0.1"
CUSTOMER_BASE_URL= BASE_URL + "/customers"
TRANSACTION_BASE_URL= BASE_URL + "/transactions"

app = FastAPI()

app.include_router(customerRouter , prefix = CUSTOMER_BASE_URL, tags = ["customers"])
app.include_router(transactionRouter , prefix = TRANSACTION_BASE_URL, tags = ["transactions"])