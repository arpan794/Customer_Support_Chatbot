from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.db_dependency import get_db
from app.models.user import User

from app.schemas.user import UserCreate, UserLogin
from app.core.security import ( hash_password, verify_password)
from app.core.jwt_handler import create_access_token


router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            details="Email already registered"
        )
    
    hased_pwd = hash_password(user.password)

    new_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hased_pwd,
        company_id=user.company_id
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }



@router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            details="Invalid email or password"
        )

    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=401,
            details="Invalid email or password"
        )
        
    access_token = create_access_token(
        data={
            "user_id": db_user.id,
            "name": db_user.name,
            "email": db_user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
   }








