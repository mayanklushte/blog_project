from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog_app'

urlpatterns = [
    path('index', views.index, name='index'),
    path('create_blog', views.create_blog, name='create_blog'),
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)