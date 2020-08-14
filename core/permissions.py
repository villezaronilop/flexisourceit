from django.conf import settings
from rest_framework import permissions


class IsUserAuthenticated(permissions.BasePermission):
    """
        Extended IsAuthenticated permission
    """

    def has_permission(self, request, view):

        if not settings.PASSWORDLESS_AUTH_ENABLED:
            return True
        return bool(request.user and request.user.is_authenticated)