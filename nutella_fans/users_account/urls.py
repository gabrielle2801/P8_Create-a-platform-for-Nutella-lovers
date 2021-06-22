from django.urls import path
# from django.conf.urls import include
# from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login_request, name='login_request'),
]
