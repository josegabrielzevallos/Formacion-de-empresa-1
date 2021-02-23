from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('assign_menu', views.assignMenu, name='assignMenu'),
    path('profile', views.profile, name='profile'),
    path('addmenu', login_required(views.AddMenu.as_view()), name='addmenu'),
    path('addrestaurant', login_required(views.AddRestaurant.as_view()), name='addrestaurant'),
    path('restaurant_profile', views.profile_restaurant, name='restaurant_profile'),
    path('pedidos', views.pedidos, name='pedidos'),
]
