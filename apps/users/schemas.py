from ninja import Schema
class UserRegisterSchema(Schema):
    username: str
    password: str
class UserLoginSchema(Schema):
    username: str
    password: str
class TokenOutSchema(Schema):
    token: str
