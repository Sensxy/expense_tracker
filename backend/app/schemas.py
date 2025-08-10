from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class ExpenseBase(BaseModel):
    amount: float
    category: str
    description: Optional[str] = None

class ExpenseCreate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str