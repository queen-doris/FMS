from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import get_db

router = APIRouter(prefix="/vehicles", tags=["vehicles"])

@router.get("/", response_model=list[schemas.Vehicle])
def read_vehicles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_vehicles(db, skip=skip, limit=limit)

@router.get("/{vehicle_id}", response_model=schemas.Vehicle)
def read_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = crud.get_vehicle(db, vehicle_id=vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.post("/", response_model=schemas.Vehicle)
def create_vehicle(vehicle: schemas.VehicleCreate, db: Session = Depends(get_db)):
    return crud.create_vehicle(db, vehicle=vehicle)

@router.put("/{vehicle_id}", response_model=schemas.Vehicle)
def update_vehicle(vehicle_id: int, vehicle: schemas.VehicleCreate, db: Session = Depends(get_db)):
    updated_vehicle = crud.update_vehicle(db, vehicle_id=vehicle_id, vehicle=vehicle)
    if not updated_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return updated_vehicle

@router.delete("/{vehicle_id}", response_model=schemas.Vehicle)
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    deleted_vehicle = crud.delete_vehicle(db, vehicle_id=vehicle_id)
    if not deleted_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return deleted_vehicle
