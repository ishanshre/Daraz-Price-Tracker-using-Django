from django.urls import path
from . import views


app_name = "scraping"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("update/", views.update_prices, name="update"),
]