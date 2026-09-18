from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('users/<str:uuid>/', views.user_detail, name='user_detail'),
]
