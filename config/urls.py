from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from apps.users.api import router as users_router
from apps.posts.api import router as posts_router
from apps.comments.api import router as comments_router
from apps.categories.api import router as categories_router

api = NinjaAPI(
    title="Blog API",
    version="1.0.0"
)

api.add_router("/users", users_router)
api.add_router("/posts", posts_router)
api.add_router("/comments", comments_router)
api.add_router("/categories", categories_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
