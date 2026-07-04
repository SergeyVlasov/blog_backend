from ninja import Router, Schema
from django.shortcuts import get_object_or_404
from apps.comments.models import Comment
from apps.posts.models import Post
from core.auth import auth
from .schemas import CommentCreateSchema, CommentUpdateSchema, CommentOutSchema
import logging

logger = logging.getLogger("apps")
router = Router(tags=["Comments"])

class MessageSchema(Schema):
    message: str

def comment_to_dict(c: Comment):
    return {
        "id": c.id,
        "text": c.text,
        "author": c.author.username,
        "post_id": c.post_id,
    }

@router.get("/", response=list[CommentOutSchema])
def list_comments(request):
    return [
        comment_to_dict(c)
        for c in Comment.objects.select_related("author").all()
    ]


@router.get("/{comment_id}", response=CommentOutSchema)
def get_comment(request, comment_id: int):
    comment = get_object_or_404(
        Comment.objects.select_related("author"),
        id=comment_id
    )
    return comment_to_dict(comment)

@router.post("/", auth=auth, response=CommentOutSchema)
def create_comment(request, data: CommentCreateSchema):
    post = get_object_or_404(Post, id=data.post_id)

    comment = Comment.objects.create(
        text=data.text,
        post=post,
        author=request.auth,
    )
    logger.info(
        f"Comment created comment_id={comment.id} post_id={post.id} user={request.auth.id}"
    )
    return comment_to_dict(comment)

@router.put("/{comment_id}", auth=auth, response=MessageSchema)
def update_comment(request, comment_id: int, data: CommentUpdateSchema):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author != request.auth:
        return 403, {"detail": "Not your comment"}
    comment.text = data.text
    comment.save()
    logger.info(
        f"Comment updated comment_id={comment.id} post_id={comment.post.id} user={request.auth.id}"
    )
    return {"message": "updated"}

@router.delete("/{comment_id}", auth=auth, response=MessageSchema)
def delete_comment(request, comment_id: int):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author != request.auth:
        return 403, {"detail": "Not your comment"}
    post_id = comment.post.id
    comment_id = comment.id
    comment.delete()
    logger.info(
        f"Comment deleted comment_id={comment_id} post_id={post_id} user={request.auth.id}"
    )

    return {"message": "deleted"}