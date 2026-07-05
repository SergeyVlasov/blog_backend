from ninja import Router
from django.shortcuts import get_object_or_404
from apps.categories.models import Category
from core.auth import auth
from ninja.errors import HttpError

def admin_required(user):
    if not user.is_staff:
        raise HttpError(403, "Admin access required")

router = Router(tags=["Categories"])
@router.get("/")
def list_categories(request):
    return list(Category.objects.values())
@router.post("/", auth=auth)
def create_category(request, name: str):
    admin_required(request.auth)
    category = Category.objects.create(name=name)
    return {"id": category.id, "name": category.name}
@router.put("/{category_id}", auth=auth)
def update_category(request, category_id: int, name: str):
    admin_required(request.auth)
    category = get_object_or_404(Category, id=category_id)
    category.name = name
    category.save()
    return {"id": category.id, "name": category.name}
@router.delete("/{category_id}", auth=auth)
def delete_category(request, category_id: int):
    admin_required(request.auth)
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return {"message": "deleted"}




    