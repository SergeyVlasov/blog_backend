from ninja import Router
from .models import Comment
from core.auth import auth

router = Router()

@router.post("/", auth=auth)
def create_comment(request, post_id: int, text: str):
    return Comment.objects.create(...)
