from django.db import models
from core.common.models import TimestampedModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Stock(TimestampedModel):
    name = models.CharField(max_length=255)
    price = models.FloatField()

    class Meta:
        db_table = "stock"

    def __str__(self):
        return f"UID: {self.id} - Stock: {self.name}"


class UserStock(TimestampedModel):
    stock = models.ForeignKey(
        "Stock", on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    action = models.CharField(max_length=255)
    quantity = models.IntegerField()

    class Meta:
        db_table = "user_stock"

    def __str__(self):
        return f"User: {self.user} - Stock: {self.stock} - Action: {self.action}"
