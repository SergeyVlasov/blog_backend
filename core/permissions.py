from ninja.errors import HttpError

def is_authenticated(request):
    if not request.user or not request.user.is_authenticated:
        raise HttpError(401, "Unauthorized")
    return True
    
def is_owner(request, obj):
    if obj.author != request.user:
        raise HttpError(403, "Forbidden")
    return True

def is_admin(request):
    if not request.user.is_staff:
        raise HttpError(403, "Admin only")
    return True

def is_owner_or_admin(request, obj):
    if obj.author == request.user or request.user.is_staff:
        return True
    raise HttpError(403, "Forbidden")
