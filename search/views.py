from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView
# Create your views here.
class search_list_view(ListView):
    queryset=Product.objects.all()
    template_name='list.html'
    def get_queryset(self,*args,**kwargs):
        request=self.request
        query=request.GET.get('q')
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        else :
            return None