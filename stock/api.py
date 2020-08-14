from core.mixins import AuthViewMixin, DefaultViewMixin
from rest_framework.generics import (CreateAPIView, ListAPIView,RetrieveAPIView)
from .serializers import (
    StockSerializer, UserStockListSerializer, UserStockCustomSerializer,
)
from core.models import (Stock, UserStock,)
from django.contrib.auth import get_user_model
from rest_framework.response import Response

User = get_user_model()

# Create your views here.


class StockView(DefaultViewMixin, ListAPIView):

    serializer_class = StockSerializer

    def get_queryset(self):
        return (
            Stock.objects.all()
            .order_by("-updated_at")
        )


class OrderStockView(DefaultViewMixin, CreateAPIView):

    serializer_class = UserStockListSerializer

    def get_queryset(self):
        return (
            UserStock.objects.all()
            .order_by("-updated_at")
        )

class UserStockListView(AuthViewMixin, ListAPIView):
    serializer_class = UserStockListSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        queryset = UserStock.objects.filter(user_id=pk)
        return queryset.order_by("-updated_at")


class UserStockView(AuthViewMixin, RetrieveAPIView):
    serializer_class = UserStockCustomSerializer
    queryset = UserStock.objects.all()

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        sid = self.kwargs.get("sid")

        queryset = UserStock.objects.filter(user_id=pk, stock_id=sid)
        queryset = queryset.order_by("-updated_at")
        match_serializer = self.get_serializer(queryset)
        return Response(match_serializer.data)
