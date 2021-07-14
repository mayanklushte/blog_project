from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.user_register, name='user_register'),
    path('user_login', views.user_login, name='user_login')
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)