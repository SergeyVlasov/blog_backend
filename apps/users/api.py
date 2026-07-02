from ninja import Router
from django.contrib.auth import authenticate
from ninja.errors import HttpError
from ninja_jwt.tokens import RefreshToken

router = Router()

@router.post("/register")
def register(request, username: str, password: str):
    ...

@router.post("/login")
def login(request, username: str, password: str):
    ...
