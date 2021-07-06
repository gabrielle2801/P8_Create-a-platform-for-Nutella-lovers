from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from product import views

urlpatterns = [
    path('product/', views.product, name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
