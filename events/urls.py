from django.urls import path, include
from rest_framework import routers
from . import views
import requests
from django.shortcuts import render

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'tasks',views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('home/', views.home, name='home'),
]

