from typing import List,Union
from pydantic import BaseModel
from datetime import datetime

class RolBase(BaseModel):
    nombre: str
    descripcion: str
    estatus:bool
    created_at:datetime
    
    
class RolCreate(RolBase):
    pass
class RolUpdate(RolBase):
    pass
class Rol(RolBase):
    ID:int
    #owner_id:int clave foranea
    
    class Config:
        orm_mode=True