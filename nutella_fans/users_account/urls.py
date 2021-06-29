from django.urls import path
from users_account import views
from users_account.views import LoginView, SignupView

urlpatterns = [
    path('', views.base, name='base'),
    path('', views.home, name='home'),
    # path('sign_up/', views.sign_up, name='sign_up'),
    # path('login/', views.login_request, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('sign_up/', SignupView.as_view(), name='sign_up'),
    path('logout/', views.logout_request, name='logout'),
]
