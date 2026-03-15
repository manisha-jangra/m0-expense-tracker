from pydantic import BaseModel
from datetime import date
 
# 1 create pydantic model
class Record(BaseModel):
    date: date
    category: str
    merchant: str
    description: str
    amount: float
