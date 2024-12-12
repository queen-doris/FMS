from pydantic import BaseModel

class VehicleBase(BaseModel):
    registration_number: str
    model: str
    owner: str
    is_active: bool = True

class VehicleCreate(VehicleBase):
    pass

class Vehicle(VehicleBase):
    id: int

    class Config:
        orm_mode = True
