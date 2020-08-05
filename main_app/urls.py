from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('city/', views.city_index, name='city_index'),
    path('profile/', views.profile, name="profile"),
    path('update/', views.update, name="update_profile")
]