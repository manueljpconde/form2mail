
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class ContactForm(BaseModel):
    name: str = Field(..., max_length=100)
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=20)
    consent_ts: Optional[str] = Field(None, max_length=50)
    subject: str = Field(..., max_length=150)
    message: str = Field(..., max_length=2000)
