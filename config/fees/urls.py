from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentFeeViewSet

router = DefaultRouter()
router.register(r'fees', StudentFeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]