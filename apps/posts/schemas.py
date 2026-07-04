from ninja import Schema
class PostCreateSchema(Schema):
    title: str
    content: str
    category_id: int | None = None
class PostUpdateSchema(Schema):
    title: str
    content: str
class PostOutSchema(Schema):
    id: int
    title: str
    content: str
    author: str