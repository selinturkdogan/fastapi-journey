from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

router = APIRouter()

@router.post("/signup")
async def sign_up(user: User):
    existing_user = await User.find_one(User.email == user.email)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists"
        )

    await user.insert()
    return {"message": "User created successfully", "email": user.email}


@router.post("/signin")
async def sign_in(user: UserSignIn):
    existing_user = await User.find_one(User.email == user.email)

    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    if existing_user.password == user.password:
        return {"message": "Login successful"}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials"
    )