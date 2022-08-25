
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path("contact/", views.contact, name="contact"),
    path("shop/", views.shop , name="shop"),
    path("cart/", views.cart, name='cart'),
    path("checkout/", views.checkout, name='checkout'),
]
