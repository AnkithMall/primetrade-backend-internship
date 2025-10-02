# app/routers/user.py
from app.auth.dependencies import require_admin
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserCreate, UserOut
from app.crud.user import create_user, get_user_by_email
from app.auth.auth import create_access_token
from app.auth.utils import verify_password
from slowapi.util import get_remote_address
from app.core.rate_limiter import limiter
from fastapi import Request

router = APIRouter()

@router.post("/register", response_model=UserOut)
@limiter.limit("5/minute")
def register_user(request: Request,user: UserCreate):
    db_user = get_user_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = create_user(user.name, user.email, user.password)
    return {
        "id": str(new_user["_id"]),
        "name": new_user["name"],
        "email": new_user["email"],
        "role": new_user["role"]
    }

@router.post("/login")
@limiter.limit("5/minute")
def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_by_email(form_data.username)
    if not user or not verify_password(form_data.password, user["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token(data={"sub": user["email"], "role": user["role"]})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/admin-only", dependencies=[Depends(require_admin)])
def admin_only():
    return {"message": "Welcome Admin!"}
