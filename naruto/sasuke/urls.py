# ninja/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ninja_list, name='ninja_list'),
    path('<int:pk>/', views.ninja_detail, name='ninja_detail'),
    path('create/', views.ninja_create, name='ninja_create'),
    path('<int:pk>/update/', views.ninja_update, name='ninja_update'),
    path('<int:pk>/delete/', views.ninja_delete, name='ninja_delete'),
]
