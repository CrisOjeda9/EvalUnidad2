from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
import crud.usuarios_roles, config.db, schemas.usuarios_roles, models.usuarios_roles
from typing import List

userRol= APIRouter()

models.usuarios_roles.Base.metadata.create_all(bind=config.db.engine)

def  get_db():
    db=config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@userRol.get("/usersroles/", response_model=List[schemas.usuarios_roles.UsuarioRol], tags=["userRol"] )
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_UserRol= crud.usuarios_roles.get_UserRol(db=db, skip=skip, limit=limit)
    return db_UserRol

@userRol.post("/usersroles/{id}", response_model=schemas.usuarios_roles.UsuarioRol, tags=["userRol"])
def read_user(id: int, db: Session = Depends(get_db)):
    db_UserRol= crud.usuarios_roles.get_UserRol(db=db, id=id)
    if db_UserRol is None:
        raise HTTPException(status_code=404, detail="Usuario-rol not found")
    return db_UserRol

@userRol.post("/usersroles/", response_model=schemas.usuarios_roles.UsuarioRol, tags=["userRol"])
def create_user(user: schemas.usuarios_roles.UsuarioRolCreate, db: Session = Depends(get_db)):
    db_UserRol = crud.usuarios_roles.get_userrol_by_userrol(db, usuario_id=user.usuario_id)
    if db_UserRol:
        raise HTTPException(status_code=400, detail="Usuario-rol existente, intenta nuevamente")
    return crud.create_UserRol(db=db, usuario_rol=user)

@userRol.put("/usersroles/{id}", response_model=schemas.usuarios_roles.UsuarioRol, tags=["userRol"])
def update_user(id: int, user: schemas.usuarios_roles.UsuarioRolUpdate, db: Session = Depends(get_db)):
    db_UserRol = crud.usuarios_roles.update_UserRol(db = db, id = id, userRol = userRol)
    if db_UserRol is None:
        raise HTTPException(status_code=404, detail="Usuario no existente, no esta actuaizado")
    return db_UserRol

@userRol.delete("/usersroles/{id}", response_model=schemas.usuarios_roles.UsuarioRol, tags=["userRol"])
def delete_user(id: int, db: Session = Depends(get_db)):
    db_UserRol = crud.usuarios_roles.delete_UserRol(db = db, id = id)
    if db_UserRol is None:
        raise HTTPException(status_code=404, detail="Usario-rol no existe, no s epudo eliminar")
    return db_UserRo