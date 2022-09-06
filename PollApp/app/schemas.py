from typing import List, Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class PollBase(BaseModel):
    title : str
    content : str

    class Config:
        orm_mode = True




class Poll(PollBase):
    owner_id : int

    class Config:
        orm_mode = True
    
class ShowPoll(Poll):
    pass

class  CreatePoll(PollBase):
    pass 

class UpdatePoll(Poll):
    pass

class DeletePoll(Poll):
    pass


class Token(BaseModel):
    access_token = str
    token_type = str

class TokenData(BaseModel):
    id: Optional[str] = None
    
class User(BaseModel):
    email : EmailStr
    password : str
   
 
    class Config:
        orm_mode = True



class ShowUser(User):
    pass

class CreateUser(User):
    pass
class UpdateUser(User):
    pass
class DeleteUser(User):
    pass

class UserOut(BaseModel):
    id : int
    email: EmailStr

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password : str

    class Config:
        orm_mode = True

