from django.conf.urls import url
from stock.api import (StockView, OrderStockView, UserStockListView, UserStockView)

urlpatterns = [
    url(r"^stock$", StockView.as_view(), name="stock-list"),
    url(r"^order/stock$", OrderStockView.as_view(), name="order-stock"),
    url(r"^user/(?P<pk>[0-9]+)/stock$", UserStockListView.as_view(), name="user-stock-list"),
    url(r"^user/(?P<pk>[0-9]+)/stock/(?P<sid>[0-9]+)$", UserStockView.as_view(), name="user-stock"),
]