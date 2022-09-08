from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.main, name='home'),
    path('shop/', views.shop, name='shop'),
    path('signup/',views.signup, name='signup')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
