from django.shortcuts import render
from django.views.generic import ListView,DetailView
from products.models import Product
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

# Create your views here.


class product_list_view(ListView):
    queryset=Product.objects.all()
    template_name='product_list.html'
    def get_context_data(self,*args,**kwargs):
        context=super(product_list_view,self).get_context_data(*args,**kwargs)
        print(context)
        return context

class product_detail_slug_view(DetailView):
    queryset=Product.objects.all()
    template_name='product_detail.html'

    def get_object(self,*args,**kwargs):
        slug=self.kwargs.get('slug')
        #instance=Product.objects.get(slug=slug)
        instance=Product.objects.filter(slug=slug).first()
        if instance is None:
            raise Http404("Dafuq! Product does not exist")
        return instance

class product_detail_view(DetailView):
    queryset=Product.objects.all()
    template_name='product_detail.html'
    def get_context_data(self,*args,**kwargs):
        context=super(product_detail_view,self).get_context_data(*args,**kwargs)
        return context

    def get_object(self,*args,**kwargs):
        pk=self.kwargs.get('pk')
        instance=Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Dafuq! Product does not exist")
        return instance
