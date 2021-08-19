from rest_framework import permissions


class AdminOrReadOnly(permissions.BasePermission):
    """Ограничение: для администратора - полный доступ,
    для остальных - только чтение."""
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_superuser)
