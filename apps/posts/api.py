from ninja import Router
from django.shortcuts import get_object_or_404
from apps.posts.models import Post
from apps.categories.models import Category
from core.auth import auth
from .schemas import PostCreateSchema, PostUpdateSchema, PostOutSchema
router = Router(tags=["Posts"])
def post_to_dict(post: Post):
    return {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "author": post.author.username,
    }
@router.get("/", response=list[PostOutSchema])
def list_posts(request):
    return [
        post_to_dict(p)
        for p in Post.objects.select_related("author").all()
    ]
@router.get("/{post_id}", response=PostOutSchema)
def get_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return post_to_dict(post)
@router.post("/", auth=auth, response=PostOutSchema)
def create_post(request, data: PostCreateSchema):
    category = None
    if data.category_id:
        category = get_object_or_404(Category, id=data.category_id)
    post = Post.objects.create(
        title=data.title,
        content=data.content,
        author=request.auth,
        category=category,
    )
    return post_to_dict(post)
@router.put("/{post_id}", auth=auth)
def update_post(request, post_id: int, data: PostUpdateSchema):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.auth:
        return 403, {"detail": "Not your post"}
    post.title = data.title
    post.content = data.content
    post.save()
    return {"message": "updated"}
@router.delete("/{post_id}", auth=auth)
def delete_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.auth:
        return 403, {"detail": "Not your post"}
    post.delete()
    return {"message": "deleted"}