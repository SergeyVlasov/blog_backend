from ninja import Router
from .models import Post
from core.auth import auth

router = Router()

@router.get("/")
def list_posts(request):
    return Post.objects.all()

@router.post("/", auth=auth)
def create_post(request, title: str, content: str):
    return Post.objects.create(
        title=title,
        content=content,
        author=request.user
    )
