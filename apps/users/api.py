from ninja import Router
from django.contrib.auth import authenticate
from ninja.errors import HttpError
from apps.users.models import User
from .schemas import UserRegisterSchema, UserLoginSchema, TokenOutSchema

router = Router(tags=["Users"])


@router.post("/register", response=TokenOutSchema)
def register(request, data: UserRegisterSchema):
    if User.objects.filter(username=data.username).exists():
        raise HttpError(400, "Username already exists")

    user = User(username=data.username)
    user.set_password(data.password)
    user.save()

    user.generate_token()

    return {"token": user.token}


@router.post("/login", response=TokenOutSchema)
def login(request, data: UserLoginSchema):
    user = authenticate(username=data.username, password=data.password)

    if not user:
        raise HttpError(401, "Invalid credentials")

    user.generate_token()

    return {"token": user.token}