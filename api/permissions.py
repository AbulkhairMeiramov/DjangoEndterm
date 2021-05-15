from rest_framework.permissions import IsAuthenticated
from utils.constants import USER_ROLE_SUPER_USER, USER_ROLE_CLIENT


class SuperUserPermission(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == USER_ROLE_SUPER_USER


class ClientPermission(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == USER_ROLE_CLIENT
