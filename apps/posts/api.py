from ninja import Router, Schema
from django.shortcuts import get_object_or_404
from apps.posts.models import Post
from apps.categories.models import Category
from core.auth import auth
from .schemas import PostCreateSchema, PostUpdateSchema, PostOutSchema
import logging

logger = logging.getLogger("apps")

router = Router(tags=["Posts"])


class MessageSchema(Schema):
    message: str


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
    post = get_object_or_404(
        Post.objects.select_related("author"),
        id=post_id
    )
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

    logger.info(
        f"Post created post_id={post.id} user={request.auth.id}"
    )

    return post_to_dict(post)


@router.put("/{post_id}", auth=auth, response=MessageSchema)
def update_post(request, post_id: int, data: PostUpdateSchema):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.auth:
        return 403, {"detail": "Not your post"}

    post.title = data.title
    post.content = data.content
    post.save()

    logger.info(
        f"Post updated post_id={post.id} user={request.auth.id}"
    )

    return {"message": "updated"}


@router.delete("/{post_id}", auth=auth, response=MessageSchema)
def delete_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.auth:
        return 403, {"detail": "Not your post"}

    post_id = post.id
    post.delete()

    logger.info(
        f"Post deleted post_id={post_id} user={request.auth.id}"
    )

    return {"message": "deleted"}