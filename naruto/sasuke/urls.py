# ninja/urls.py
from django.urls import path
from . import views

urlpatterns = [


    path('', views.ninja_list, name='ninja_list'),
    path('<int:pk>/', views.ninja_detail, name='ninja_detail'),
    path('create/', views.ninja_create, name='ninja_create'),
    path('<int:pk>/update/', views.ninja_update, name='ninja_update'),
    path('<int:pk>/delete/', views.ninja_delete, name='ninja_delete'),
path('missions/', views.mission_list, name='mission_list'),
    path('missions/create/', views.mission_create, name='mission_create'),
    path('missions/<int:pk>/', views.mission_detail, name='mission_detail'),
    path('missions/<int:pk>/edit/', views.mission_update, name='mission_update'),
    path('missions/<int:pk>/delete/', views.mission_delete, name='mission_delete'),

    path('jutsu_create', views.jutsu_create, name='jutsu_create'),
    path('team_create', views.team_create, name='team_create'),
]
