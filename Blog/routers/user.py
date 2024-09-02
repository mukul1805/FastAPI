
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database,models
from ..hashing import Hash       


router = APIRouter(
    # tags=['User']       #we can directly use it here only
    # prefix="/blog"      we can remove blog from below
)

get_db= database.get_db

# to create a new User

@router.post('/user',response_model=schemas.showUser,tags=['User'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    # new_user = models.User(request)     #only request will not work, use 
    # hashed_password = pwd_cxt.hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)        #refresh at new_user
    return new_user

@router.get('/user',tags=['User'])
def all_user(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.get('/user/{id}',response_model=schemas.showUser,tags=['User'])
def user_by_id(id=int, db: Session = Depends(get_db)):
    user_with_id = db.query(models.User).filter(models.User.id == id).first()   #where condition in sqlalchemy
    if not user_with_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not available!")
    return user_with_id