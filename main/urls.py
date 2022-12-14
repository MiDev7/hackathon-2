from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('signup/',views.signup, name='signup'),
    path('cart/',views.cart,name='cart'),
    path('updateCart/',views.updateCart, name="update_cart"),
    path('checkout/',views.checkout, name="update_cart"),
    path('process_order/',views.processOrder, name="processOrder"),
    path('home/', views.home, name='home'),
    path('login/', views.loginPage, name='login'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

