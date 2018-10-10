from products.api.serializer import ProductSerializer
from rest_framework import generics
from products.models import Product

class ProductRud(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field    ="slug"
    serializer_class=ProductSerializer
    def get_queryset(self):
        return Product.objects.all()
        
