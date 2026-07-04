from ninja import Schema
class CommentCreateSchema(Schema):
    post_id: int
    text: str
class CommentUpdateSchema(Schema):
    text: str
class CommentOutSchema(Schema):
    id: int
    text: str
    author: str
    post_id: int