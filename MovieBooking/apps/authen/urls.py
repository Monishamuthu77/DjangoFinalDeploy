from django.contrib import admin
from . import views
from django.urls import path
from django.views.generic import TemplateView, View
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path('profilepage/', views.profilepage, name='profilepage'),
    path('logout/', views.logout_request, name='logout'),
]

