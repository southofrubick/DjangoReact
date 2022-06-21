from django.urls import path, include
from rest_framework import routers

from .views import ProductView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'products', ProductView, 'products')

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]