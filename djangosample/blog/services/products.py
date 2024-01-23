from django.db.models import QuerySet
from ..models import Product


def create_product(name: str) -> QuerySet[Product]:
    return Product.objects.create(name=name)

