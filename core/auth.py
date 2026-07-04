from ninja.security import HttpBearer
from apps.users.models import User

class TokenAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            return User.objects.get(token=token)
        except User.DoesNotExist:
            return None
auth = TokenAuth()