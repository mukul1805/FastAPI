from sqlalchemy.orm import Session
from .. import models
from .. import schemas
from fastapi import HTTPException, status
from ..hashing import Hash       


def create(request: schemas.User,db: Session):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)        #refresh at new_user
    return new_user

def show_all(db:Session):
    users = db.query(models.User).all()
    return users

def show_user(id:int, db:Session):
    user_with_id = db.query(models.User).filter(models.User.id == id).first()   #where condition in sqlalchemy
    if not user_with_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not available!")
    return user_with_id