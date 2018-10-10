from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from homio import views
from products.views import product_list_view
from django.conf import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.product_list_view.as_view()),
    url(r'^register/',views.register_page),
    url(r'^login/$',views.login_page),
    url(r'^cart/',views.cart),
    url(r'^about_us/',views.about_us),
    url(r'^products/',include('products.urls')),
    url(r'^search/',include('search.urls')),
    url(r'^logout/$', LogoutView.as_view(template_name='index.html'), name="logout"),
    url(r'^api/pro/',include('products.api.urls')),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)