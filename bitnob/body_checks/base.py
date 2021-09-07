from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    email: str
    firstName: str
    lastName: str
    phone: str
    countryCode: str