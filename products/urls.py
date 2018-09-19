from django.conf.urls import url,include
from products.views import product_list_view,product_detail_slug_view,product_detail_view


urlpatterns = [
    url(r'^$',product_list_view.as_view()),
    url(r'^(?P<pk>\d+)/$',product_detail_view.as_view()),
    url(r'^(?P<slug>[\w-]+)/$',product_detail_slug_view.as_view()),
    
]