from typing import Optional

from pydantic import BaseModel, EmailStr, Field, validator


class User(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    age: Optional[int] = Field(None, gt=0, lt=150)
    email: EmailStr
    is_active: bool = True

    @validator("name")
    def name_must_be_alpha(cls, v):
        if not v.replace(" ", "").isalpha():
            raise ValueError("Name must contain only letters and spaces")
        return v
