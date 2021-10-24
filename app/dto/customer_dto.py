from pydantic import BaseModel

class CustomerDto(BaseModel):
    name: str
    email: str
