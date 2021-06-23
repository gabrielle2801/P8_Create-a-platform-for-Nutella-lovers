from django.urls import path

from users_account import views

urlpatterns = [
    path('', views.base, name='base'),
    path('', views.home, name='home'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
]
