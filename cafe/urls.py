from django.urls import path
from . import views
from .views import (
    home_view, signup_view, login_view, logout_view,
    menu_view, contact, place_order_view,
    order_success, reserve_table
)

urlpatterns = [
    path('home', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('menu/', menu_view, name='menu'),
    path('order/', place_order_view, name='place_order'),
    
    path('order-success/', order_success, name='order_success'),
    path('create_order/', views.create_order, name='create_order'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('contact/', contact, name='contact'),
    path('reserve/', reserve_table, name='reservation'),
]
