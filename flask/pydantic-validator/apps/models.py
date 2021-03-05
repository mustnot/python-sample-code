import re
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, validator
from pydantic.types import constr

class User(BaseModel):
    name: str
    email: str
    username: constr(min_length=2, max_length=255)
    sign_dtime: Optional[datetime] = datetime.now()

    @validator('email')
    def email_validator(cls, v):
        email_regex = re.compile("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?")
        if not email_regex.fullmatch(v):
            raise ValueError("email do not match")
        return v
    
    