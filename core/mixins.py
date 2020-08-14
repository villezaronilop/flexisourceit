from django.conf import settings
from core.permissions import IsUserAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.response import Response


class AuthViewMixin:
    permission_classes = (IsUserAuthenticated,)


class DefaultViewMixin(AuthViewMixin):

    _success_message = {"detail": settings.MSG_TRANSACT_SUCCESS, "code": 0}

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        self._success_message.update({"code": HTTP_201_CREATED})
        return Response(self._success_message, status=HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        self._success_message.update({"code": HTTP_200_OK})
        return Response(self._success_message, status=HTTP_200_OK)