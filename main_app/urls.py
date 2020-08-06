from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('city/', views.city_index, name='city_index'),
    path('city/detail/', views.city_detail, name="city_detail"),
    path('city/post/', views.city_post, name="city_post"),
    path('profile/<int:user_id>', views.profile, name="profile"),
    path('profile/<int:user_id>/update/', views.update, name="update_profile"),
]