from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('favourite/<int:product_id>/', views.favourite_product, name='favourite_product'),
    path('user_favourites/', views.user_favourites, name='user_favourites'),
]