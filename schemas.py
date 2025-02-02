from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    is_active: bool = True


class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    name: str 
    email: str 


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
