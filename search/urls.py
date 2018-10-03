from django.conf.urls import url,include
from search.views import search_list_view


urlpatterns = [
    url(r'^$',search_list_view.as_view(),name='query'),
]