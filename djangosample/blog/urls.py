from django.urls import path
from .apis.product import ProductApi


urlpatterns = [
    path('product/', ProductApi.as_view(), name='product')
]
