from products.api.views import ProductRud
from django.contrib import admin
from django.conf.urls import url,include

urlpatterns=[
    url(r'^(?P<slug>[\w-]+)/$', ProductRud.as_view(), name="ProductRud")
]