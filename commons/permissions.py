from rest_framework import permissions


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


class IsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser


# custom permission "IsOnlySuperUserAndOwnerCanDelete" only the owner and superusers can delete a cohort
class IsOnlySuperUserAndOwnerCanDelete(permissions.BasePermission):
    delete_method = "DELETE"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.method != self.delete_method:
            return True
        if request.user.is_superuser and request.method == self.delete_method:
            return True
        if obj.owner == request.user and request.method == self.delete_method:
            return True

        return False


# custom permission "IsOnlySuperUserAndOwnerAccessComments" only the owner and superusers can do any request on
# cohort's comments
class IsOnlySuperUserAndOwnerAccessComments(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if obj.owner == request.user:
            return True

        return False
