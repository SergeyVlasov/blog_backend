from ninja import Router
from django.shortcuts import get_object_or_404
from apps.categories.models import Category
from core.auth import auth
router = Router(tags=["Categories"])
@router.get("/")
def list_categories(request):
    return list(Category.objects.values())
@router.post("/", auth=auth)
def create_category(request, name: str):
    category = Category.objects.create(name=name)
    return {"id": category.id, "name": category.name}
@router.delete("/{category_id}", auth=auth)
def delete_category(request, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return {"message": "deleted"}




    