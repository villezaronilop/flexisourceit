from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.models import (Stock, UserStock,)

User = get_user_model()


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ("id", "name", "price")


class UserStockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStock
        fields = ("user", "stock", "quantity", "action",)

class UserStockCustomSerializer(serializers.ModelSerializer):
    sell = serializers.SerializerMethodField()
    buy = serializers.SerializerMethodField()

    class Meta:
        model = UserStock
        fields = ("sell","buy")

    def sum_amount(self, obj, action):
        return sum((
            i.quantity * i.stock.price
            for i in obj
            if i.action == action
        ))

    def get_buy(self, obj):
        return self.sum_amount(obj, "buy")

    def get_sell(self, obj):
        return self.sum_amount(obj, "sell")
