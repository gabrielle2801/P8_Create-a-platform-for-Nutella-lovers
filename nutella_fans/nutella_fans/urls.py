"""nutella_fans URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
<<<<<<< HEAD
from users_account import views
=======
from django.views.generic.base import TemplateView
# from users_account import views
>>>>>>> authentification

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users_account.urls')),
<<<<<<< HEAD
    path('sign_up', views.sign_up, name='sign_up'),
    path('', include('nutella_fans.urls')),
=======
    path('', TemplateView.as_view(template_name='base.html'), name='base'),
    path('account/', include('django.contrib.auth.urls')),
    # path('', include('product.urls'))
>>>>>>> authentification

]
