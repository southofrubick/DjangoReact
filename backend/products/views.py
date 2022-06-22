from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import ProductSerializer
from .models import Product

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    